# from rest_framework import serializers
# from .models import TimeSheet, TimeInOut
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class TimeSheetListSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.get_id_and_username')

#     class Meta:
#         model = TimeSheet
#         fields = '__all__'


# class TimeInOutSerializer(serializers.ModelSerializer):
#     total_hours = serializers.ReadOnlyField()
#     date = serializers.ReadOnlyField(source='date.date')

#     class Meta:
#         model = TimeInOut
#         # exclude = ['date']
#         fields = '__all__'


# class TimeSheetSerializer(serializers.ModelSerializer):
    
#     time_in_out = TimeInOutSerializer(many=True)

#     class Meta:
#         model = TimeSheet
#         exclude = ['user']


# class TimeSheetUserSerializer(serializers.ModelSerializer):
    
#     time_sheets = TimeSheetSerializer(many=True)

#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'employee_id',
#             'username',
#             'time_sheets'
#         ]
