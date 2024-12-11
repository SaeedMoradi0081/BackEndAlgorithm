from rest_framework import viewsets
from .serializers import CriticismAndSuggestionsSerializer
from .models import Cas

# Create your views here.

class CriticismAndSuggestionsViewSet(viewsets.ModelViewSet):
    queryset = Cas.objects.all().order_by('id')
    serializer_class = CriticismAndSuggestionsSerializer
