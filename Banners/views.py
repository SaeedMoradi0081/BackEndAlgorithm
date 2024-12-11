from rest_framework import viewsets
from .models import Banner
from .serializers import BannerSerializer


# Create your views here.

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('id')
    serializer_class = BannerSerializer

