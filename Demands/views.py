from rest_framework import viewsets

from Demands.models import Demand
from Demands.serializers import DemandSerializer


# Create your views here.
class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all().order_by('id')
    serializer_class = DemandSerializer
