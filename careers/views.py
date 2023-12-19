from .serializers import *
from .models import Careers
from rest_framework import generics, permissions
from django.utils import timezone

class CareersList(generics.ListCreateAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersList_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        
        if self.request.method == 'POST':
            return CareersCreate_Serializer
        
        return super().get_serializer_class()

class CareersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersDetail_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the instance using the default get_object method
        queryset = self.queryset.get(pk=instance.pk)  # Retrieve the queryset using the primary key of the instance
        if queryset.career_status == 'Probationary' and queryset.end_date:
            if queryset.end_date <= timezone.now():
                queryset.career_status = 'Regular'
                
        if queryset.career_status == 'Contractual' and queryset.end_date:
            if queryset.end_date <= timezone.now():
                queryset.career_status = 'Regular'
        
        instance.save()
        return self.retrieve(request, *args, **kwargs)
