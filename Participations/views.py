from rest_framework import viewsets
from .models import Participation
from .serializers import ParticipationSerializer


# Create your views here.

class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all().order_by('id')
    serializer_class = ParticipationSerializer
