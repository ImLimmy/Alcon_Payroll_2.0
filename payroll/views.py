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
