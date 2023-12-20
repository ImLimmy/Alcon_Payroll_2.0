from rest_framework import generics, permissions

from .serializers import *
from .cash_advance_models import CashAdvanceForm
from .half_day_models import HalfDayForm
from .leave_models import LeaveForm
from .overtime_models import OverTimeForm
from .tempshift_models import TemporaryShiftForm

# Cash Advance Form
class CashAdvanceList(generics.ListCreateAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()
    
class CashAdvanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CashAdvanceForm.objects.all()
    serializer_class = CashAdvanceDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CashAdvanceCreateSerializer
        return super().get_serializer_class()
    
# Half-Day Form
class HalfDayList(generics.ListCreateAPIView):
    queryset = HalfDayForm.objects.all()
    serializer_class = HalfDayListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return HalfDayCreateSerializer
        return super().get_serializer_class()
    
class HalfDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HalfDayForm.objects.all()
    serializer_class = HalfDayDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return HalfDayCreateSerializer
        return super().get_serializer_class()
    
# Leave Form
class LeaveList(generics.ListCreateAPIView):
    queryset = LeaveForm.objects.all()
    serializer_class = LeaveListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return LeaveCreateSerializer
        return super().get_serializer_class()
    
class LeaveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeaveForm.objects.all()
    serializer_class = LeaveDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return LeaveCreateSerializer
        return super().get_serializer_class()
    
# OverTime Form
class OverTimeList(generics.ListCreateAPIView):
    queryset = OverTimeForm.objects.all()
    serializer_class = OverTimeListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return OverTimeCreateSerializer
        return super().get_serializer_class()
    
class OverTimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OverTimeForm.objects.all()
    serializer_class = OverTimeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return OverTimeCreateSerializer
        return super().get_serializer_class()
    
# Temporary Shift Form
class TemporaryShiftList(generics.ListCreateAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()
    
class TemporaryShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TemporaryShiftForm.objects.all()
    serializer_class = TemporaryShiftDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return TemporaryShiftCreateSerializer
        return super().get_serializer_class()