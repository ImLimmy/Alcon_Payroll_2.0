from rest_framework import generics, permissions

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
    TemporaryShiftListSerializer,
    TemporaryShiftDetailSerializer,
    TemporaryShiftCreateSerializer,
)
from .cash_advance_models import CashAdvanceForm
from .half_day_models import HalfDayForm
from .leave_models import LeaveForm
from .overtime_models import OverTimeForm
from .tempshift_models import TemporaryShiftForm
from api.mixins import UserPermissionMixin, AdminPermissionMixin

# Cash Advance Form
class CashAdvanceList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceListSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()
    
class CashAdvanceDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceDetailSerializer
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()
    
# Half-Day Form
class HalfDayList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = HalfDayForm.objects.all()
    serializer_class = HalfDayListSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return HalfDayCreateSerializer
        return super().get_serializer_class()
    
class HalfDayDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = HalfDayForm.objects.all()
    serializer_class = HalfDayDetailSerializer
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return HalfDayCreateSerializer
        return super().get_serializer_class()
    
# Leave Form
class LeaveList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = LeaveForm.objects.all()
    serializer_class = LeaveListSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveCreateSerializer
        return super().get_serializer_class()
    
class LeaveDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveForm.objects.all()
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
    
class OverTimeDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = OverTimeForm.objects.all()
    serializer_class = OverTimeDetailSerializer
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return OverTimeCreateSerializer
        return super().get_serializer_class()
    
# Temporary Shift Form
class TemporaryShiftList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftListSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()
    
class TemporaryShiftDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftDetailSerializer
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()