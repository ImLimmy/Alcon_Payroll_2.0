from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
import pandas as pd
from django import forms
from django.utils import timezone
from rest_framework.decorators import permission_classes

from django.contrib.auth import get_user_model
from .models import TimeSheet, TimeInOut
from .serializers import TimeSheetSerializer, TimeInOutSerializer, TimeSheetListSerializer, TimeSheetUserSerializer
from api.mixins import UserPermissionMixin, AdminPermissionMixin
from datetime import time as dtime

User = get_user_model()


class UploadFileForm(forms.Form):
    file_upload = forms.FileField()


class TimeInOutList(UserPermissionMixin, generics.ListAPIView): 
    queryset = TimeInOut.objects.all()
    serializer_class = TimeInOutSerializer


class TimeSheetUserList(UserPermissionMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = TimeSheetUserSerializer


class TimeSheetUserDetail(UserPermissionMixin, generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = TimeSheetUserSerializer


class TimeSheetList(UserPermissionMixin, generics.ListAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetListSerializer


class ProcessPunchRecord(APIView):

    @permission_classes([AdminPermissionMixin])
    def post(self, request, format=None):

        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            uploaded_file = upload_form.cleaned_data['file_upload']
            df = pd.read_excel(
                uploaded_file, sheet_name='Punch Record', keep_default_na=False)

            for index, row in df.iterrows():
                if row['Staff Code'] != '' and User.objects.filter(employee_id=row['Staff Code']).exists():
                    employee_id = row['Staff Code']
                    name = row['Name']
                    time_log = {}
                    for date in df.columns[2:]:
                        try:
                            punch_times = row[date].split('\n')
                        except:
                            punch_times = [row[date]]
                        if len(punch_times) == 1:
                            if punch_times[0] == '':
                                time_log[date] = {
                                    'Time In': None, 'Time Out': None}
                            else:
                                time_log[date] = {
                                    'Time In': punch_times[0], 'Time Out': None}
                        else:
                            time_log[date] = {
                                'Time In': punch_times[0], 'Time Out': punch_times[-1]}
                    user = User.objects.get(
                        employee_id=employee_id)
                    flexi_counter = 3  # must reset after every month or cutoff?

                    for date, time in time_log.items():
                        time_sheet = TimeSheet.objects.create(
                            user=user,
                            date=f"{timezone.now().year}-{date}"
                        )
                        category = "on-time" if time['Time In'] is not None and time['Time Out'] is not None else "late"
                        if time['Time In'] is not None and time['Time Out'] is not None:
                            TimeInOut.objects.create(
                                date=time_sheet, time_in=time['Time In'], time_out=time['Time Out']
                            )
                        elif time['Time In'] is not None:
                            TimeInOut.objects.create(
                                date=time_sheet, time_in=time['Time In']
                            )
                        elif time['Time Out'] is not None:
                            TimeInOut.objects.create(
                                date=time_sheet, time_out=time['Time Out']
                            )

                        for time_in_out in time_sheet.time_in_out.all():

                            d = time_in_out.time_in
                            if d > dtime(8, 30):
                                if d > dtime(10, 30):
                                    if flexi_counter > 0:
                                        time_in_out.category = "Flexi + Late"
                                        flexi_counter -= 1
                                    else:
                                        time_in_out.category = f"Late and Number of Flexi is {
                                            flexi_counter}"
                                elif d > dtime(9, 0):
                                    if flexi_counter > 0:
                                        time_in_out.category = "Flexi"
                                        flexi_counter -= 1
                                    else:
                                        time_in_out.category = f"Late and Number of Flexi is {
                                            flexi_counter}"
                                else:
                                    time_in_out.category = "Late"
                            else:
                                time_in_out.category = "On-Time"

                            time_in_out.save()

            return Response("Data processed and saved to database", status=status.HTTP_200_OK)
        return Response(upload_form.errors, status=status.HTTP_400_BAD_REQUEST)
