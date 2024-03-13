from users.models import User
from users.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from users.departments.models import Department
from users.departments.serializers import DepartmentList_Serializer, DepartmentDetail_Serializer
from users.positions.models import Position
from users.positions.serializers import PositionList_Serializer, PositionDetail_Serializer
from api.mixins import UserPermissionMixin, AdminPermissionMixin

# Login


class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        data = {}
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            serializer = UserDetailSerializer(user)
            user_data = serializer.data
            data['token'] = token.key
            data['user'] = user_data
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Register


class Register(AdminPermissionMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Register_Serializer

    def data(self):
        data = {}
        if Register_Serializer.is_valid():
            account = Register_Serializer.save()
            data['response'] = 'User created successfully'
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = Register_Serializer.errors
        return Response(data)

# Logout


class Logout(APIView):
    permission_classes = (permissions.IsAuthenticated, )

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


    
class UserDetail(UserPermissionMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'employee_id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'DELETE'] and self.request.user.is_staff:
            return UserDetailSerializer
        return super().get_serializer_class()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, employee_id=self.kwargs.get('employee_id'))
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


        

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

# Upload Image


@api_view(['POST'])
def uploadimage(request):
    data = request.data

    obj_id = data['obj_id']
    obj = User.objects.get(id=obj_id)
    obj.image = request.FILES.get('image')
    obj.save()

    return Response({'image': obj.image.url})
