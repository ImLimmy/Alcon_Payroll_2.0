from rest_framework import serializers

from .models import User, Privilege
from timesheets.serializers import TimeSheetSerializer

# User


class UserSerializer(serializers.ModelSerializer):
    basic_salary_per_month = serializers.ReadOnlyField()
    department = serializers.SlugRelatedField(
        slug_field='department', read_only=True)
    position = serializers.SlugRelatedField(
        slug_field='position', read_only=True)
    shift = serializers.SlugRelatedField(
        slug_field='shift_name', read_only=True)
    career = serializers.SlugRelatedField(
        slug_field='career_status', read_only=True)
    incentives = serializers.SlugRelatedField(
        slug_field='incentive_name', many=True, read_only=True)
    deductions = serializers.SlugRelatedField(
        slug_field='deduction_name', many=True, read_only=True)
    privilege = serializers.StringRelatedField()

    class Meta:
        model = User
        exclude = [
            'password',

            'last_login',
            'created_at',
            'updated_at',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions',
        ]


class UserListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    department = serializers.SlugRelatedField(
        slug_field='department', read_only=True)
    position = serializers.SlugRelatedField(
        slug_field='position', read_only=True)
    employment_date = serializers.StringRelatedField(read_only=True)
    career = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'image',
            'employee_id',
            'full_name',
            'department',
            'position',
            'employment_date',
            'career',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    basic_salary_per_month = serializers.ReadOnlyField()
    full_name = serializers.CharField(read_only=True)
    department = serializers.SlugRelatedField(
        slug_field='department', read_only=True)
    position = serializers.SlugRelatedField(
        slug_field='position', read_only=True)
    shift = serializers.SlugRelatedField(
        slug_field='shift_name', read_only=True)
    career = serializers.SlugRelatedField(
        slug_field='career_status', read_only=True)
    incentives = serializers.SlugRelatedField(
        slug_field='incentive_name', many=True, read_only=True)
    deductions = serializers.SlugRelatedField(
        slug_field='deduction_name', many=True, read_only=True)
    privilege = serializers.StringRelatedField()

    pag_ibig_contribution = serializers.StringRelatedField()
    philhealth_contribution = serializers.StringRelatedField()
    sss_contribution = serializers.StringRelatedField()
    

    pag_ibig_contributions = serializers.ReadOnlyField()
    phil_health_contributions = serializers.ReadOnlyField()
    sss_contributions = serializers.ReadOnlyField()

    time_sheets = TimeSheetSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = [
            'password',

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
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
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
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists'})
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
