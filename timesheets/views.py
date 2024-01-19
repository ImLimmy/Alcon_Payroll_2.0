from rest_framework import generics

from .models import TimeSheet
from .serializers import TimeSheetSerializer

class TimeSheetList(generics.ListAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
    
    