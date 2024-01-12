from rest_framework import generics
from rest_framework.response import Response

from .models import (
    PagIbig,
    PhilHealth,
    SSS,
)
from .serializers import (
    PagIbigSerializer,
    PhilHealthSerializer,
    SSSSerializer,
)
from api.mixins import UserPermissionMixin, AdminPermissionMixin

# PagIbig


class PagIbigList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = PagIbig.objects.all()
    serializer_class = PagIbigSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return PagIbigSerializer
        return super().get_serializer_class()


class PagIbigDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PagIbig.objects.all()
    serializer_class = PagIbigSerializer

# PhilHealth


class PhilHealthList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = PhilHealth.objects.all()
    serializer_class = PhilHealthSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return PhilHealthSerializer
        return super().get_serializer_class()


class PhilHealthDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PhilHealth.objects.all()
    serializer_class = PhilHealthSerializer

# SSS


class SSSList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = SSS.objects.all()
    serializer_class = SSSSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return SSSSerializer
        return super().get_serializer_class()


class SSSDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SSS.objects.all()
    serializer_class = SSSSerializer
