from .models import User, Privilege
from rest_framework import serializers

# User
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'created_at',
            'updated_at',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
        ]
        
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
        ]
        
# Admin
class AdminCreateAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_superuser',
        ]
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class AdminCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
# Register
class Register_Serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    is_superuser = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            is_superuser=self.validated_data['is_superuser']
        )
        account.set_password(password)
        account.save()
        return account
  
# Privilege  
class PrivilegeList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Privilege
        fields = '__all__'
        
class PrivilegeDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Privilege
        fields = '__all__'