from rest_framework import generics

from .models import Incentives, Deductions
from .serializers import *
from api.mixins import UserPermissionMixin, AdminPermissionMixin


class IncentivesList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Incentives.objects.all()
    serializer_class = IncentivesListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return IncentivesSerializer
        return super().get_serializer_class()


class IncentivesDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Incentives.objects.all()
    serializer_class = IncentivesDetailSerializer


class DeductionsList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Deductions.objects.all()
    serializer_class = DeductionsListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return DeductionsSerializer
        return super().get_serializer_class()


class DeductionsDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Deductions.objects.all()
    serializer_class = DeductionsDetailSerializer
