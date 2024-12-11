from rest_framework import serializers
from Demands.models import Demand


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'
