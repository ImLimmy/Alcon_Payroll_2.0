from users.models import User
from users.serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.departments.models import Department
from users.departments.serializers import DepartmentList_Serializer, DepartmentDetail_Serializer
from users.positions.models import Position
from users.positions.serializers import PositionList_Serializer, PositionDetail_Serializer

# Register
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Register_Serializer
    permission_classes = [permissions.IsAdminUser]
    
    def data(self):
        data = {}
        if Register_Serializer.is_valid():
            account = Register_Serializer.save()
            data ['response'] = 'User created successfully'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = Register_Serializer.errors
        return Response(data)
    
# Logout
class Logout(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'response': 'Successfully logged out'})

# Departments
class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentList_Serializer
    permission_classes = [permissions.IsAuthenticated]
    
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetail_Serializer
    permission_classes = [permissions.IsAuthenticated]

# Positions
class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionList_Serializer
    permission_classes = [permissions.IsAuthenticated]

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionDetail_Serializer
    permission_classes = [permissions.IsAuthenticated]

# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# Admin
class AdminCreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminCreateUserSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        user = User.objects.create_user(**serializer.validated_data)
        user.set_password(password)
        user.save()
        return user
