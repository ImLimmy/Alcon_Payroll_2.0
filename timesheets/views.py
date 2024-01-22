from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django import forms

from .models import TimeLogs

class UploadFileForm(forms.Form):
    file_upload = forms.FileField()

class ProcessPunchRecord(APIView):
    def post(self, request, format=None):
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            uploaded_file = upload_form.cleaned_data['file_upload']
            df = pd.read_excel(uploaded_file, sheet_name='Punch Record', keep_default_na=False)
            
            for index, row in df.iterrows():
                if row['Staff Code'] != '':
                    employee_id = row['Staff Code']
                    name = row['Name']
                    time_log = {}
                    for date in df.columns[2:]:
                        punch_times = row[date].split('\n')
                        if len(punch_times) == 1:
                            if punch_times[0] == '':
                                time_log[date] = {'Time In': None, 'Time Out': None}
                            else:
                                time_log[date] = {'Time In': punch_times[0], 'Time Out': None}
                        else:
                            time_log[date] = {'Time In': punch_times[0], 'Time Out': punch_times[-1]}
                    
                    processed_record = TimeLogs(employee_id=employee_id, name=name, time_log=time_log)
                    processed_record.save()

            return Response("Data processed and saved to database", status=status.HTTP_200_OK)
        else:
            return Response(upload_form.errors, status=status.HTTP_400_BAD_REQUEST)