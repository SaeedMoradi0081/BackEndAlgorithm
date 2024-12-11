from rest_framework import serializers

from Accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'nationality_code','first_name', 'last_name', 'password','picture']
