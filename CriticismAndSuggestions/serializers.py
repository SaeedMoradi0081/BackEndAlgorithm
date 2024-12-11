from rest_framework import serializers
from .models import Cas


class CriticismAndSuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cas
        fields = '__all__'

