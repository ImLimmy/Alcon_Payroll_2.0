from .serializers import *
from rest_framework import generics, permissions

from .models import Shift

class ShiftList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ShiftCreateSerializer
        return super().get_serializer_class()
        
class ShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftDetailSerializer
    permission_classes = [permissions.IsAuthenticated]