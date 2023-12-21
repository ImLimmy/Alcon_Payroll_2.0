from users.models import User
from users.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.departments.models import Department
from users.departments.serializers import DepartmentList_Serializer, DepartmentDetail_Serializer
from users.positions.models import Position
from users.positions.serializers import PositionList_Serializer, PositionDetail_Serializer
from api.mixins import UserPermissionMixin, AdminPermissionMixin

# Register
class Register(AdminPermissionMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Register_Serializer
    
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
class Logout(UserPermissionMixin, generics.GenericAPIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'response': 'Successfully logged out'})

# Departments
class DepartmentList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentList_Serializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return DepartmentDetail_Serializer
        return super().get_serializer_class()
    
class DepartmentDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentDetail_Serializer

# Positions
class PositionList(UserPermissionMixin, generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionList_Serializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST' and self.request.user.is_staff:
            return PositionDetail_Serializer
        return super().get_serializer_class()

class PositionDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionDetail_Serializer

# User
class UserList(UserPermissionMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
class UserDetail(UserPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'PUT' and self.request.user.is_staff:
            return UserDetailSerializer
        if self.request.method == 'DELETE' and self.request.user.is_staff:
            return UserDetailSerializer
        return super().get_serializer_class()
    
# Admin
class AdminCreateUser(AdminPermissionMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminCreateUserSerializer
    
    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        user = User.objects.create_user(**serializer.validated_data)
        user.set_password(password)
        user.save()
        return user

# Privilege
class PrivilegeList(AdminPermissionMixin, generics.ListAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeList_Serializer
    
class PrivilegeDetail(AdminPermissionMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeDetail_Serializer