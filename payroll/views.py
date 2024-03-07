<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.
from .models import Payroll
from .serializers import PayrollListSerializer, PayrollUserSerializer
from timesheets.models import TimeSheet

class PayrollList(generics.ListAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollListSerializer
    
class PayrollUser(generics.RetrieveUpdateAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = PayrollUserSerializer
=======
from api.mixins import AdminPermissionMixin
from rest_framework import generics

from .serializers import (
    PayrollSerializer,
    PayrollDetailSerializer,
)
from .models import Payroll


class PayrollList(AdminPermissionMixin, generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


class PayrollDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollDetailSerializer
>>>>>>> exp_back_end
