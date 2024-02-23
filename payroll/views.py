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