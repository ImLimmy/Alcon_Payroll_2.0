from rest_framework import generics, permissions

from .call_approval_forms import CashAdvanceForm, From_to, TemporaryShiftForm, OverTimeForm
from .leave_models import  LeaveRequestForm, HalfDayRequestForm
from .serializers import (
    CashAdvanceListSerializer,
    CashAdvanceDetailSerializer,
    CashAdvanceCreateSerializer,
    HalfDayListSerializer,
    HalfDayDetailSerializer,
    HalfDayCreateSerializer,
    LeaveListSerializer,
    LeaveDetailSerializer,
    LeaveCreateSerializer,
    OverTimeListSerializer,
    OverTimeDetailSerializer,
    OverTimeCreateSerializer,
    KpiListSerializer,
    KpiDetailSerializer,
    KpiCreateSerializer,
    TemporaryShiftListSerializer,
    TemporaryShiftDetailSerializer,
    TemporaryShiftCreateSerializer,
)
from .kpi_models import Kpi
from api.mixins import UserPermissionMixin, AdminPermissionMixin
from rest_framework.response import Response


# Cash Advance Form


class CashAdvanceList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CashAdvanceDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()

# Half-Day Form


class HalfDayList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = HalfDayRequestForm.objects.all()
    serializer_class = HalfDayListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return HalfDayCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class HalfDayDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = HalfDayRequestForm.objects.all()
    serializer_class = HalfDayDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return HalfDayCreateSerializer
        return super().get_serializer_class()


# Undertime Form

class UnderTimeList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = LeaveRequestForm.objects.all()
    serializer_class = LeaveListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveCreateSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
class UnderTimeDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequestForm.objects.all()
    serializer_class = LeaveDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return LeaveCreateSerializer
        return super().get_serializer_class()


# Leave Form


class LeaveList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = LeaveRequestForm.objects.all()
    serializer_class = LeaveListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveCreateSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    # def list(self, request, *args, **kwargs):
    #     user = request.user
    #     image_of_user = user.image

    #     # Serialize the queryset
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)

    #     # Construct the response data
    #     data = serializer.data
    #     for item in data:
    #         item['image_of_user'] = image_of_user
        
        # return Response(data)
        


class LeaveDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveRequestForm.objects.all()
    serializer_class = LeaveDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return LeaveCreateSerializer
        return super().get_serializer_class()

# OverTime Form


class OverTimeList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = OverTimeForm.objects.all()
    serializer_class = OverTimeListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OverTimeCreateSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OverTimeDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = OverTimeForm.objects.all()
    serializer_class = OverTimeDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return OverTimeCreateSerializer
        return super().get_serializer_class()

# Kpi Form


class KpiList(AdminPermissionMixin, generics.ListCreateAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return KpiCreateSerializer
        return super().get_serializer_class()


class KpiDetail(AdminPermissionMixin, generics.RetrieveDestroyAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiDetailSerializer


class KpiUpdate(AdminPermissionMixin, generics.UpdateAPIView):
    queryset = Kpi.objects.all()
    serializer_class = KpiCreateSerializer

# Temporary Shift Form


class TemporaryShiftList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(temporary_shift_user=self.request.user)

class TemporaryShiftDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftDetailSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()
