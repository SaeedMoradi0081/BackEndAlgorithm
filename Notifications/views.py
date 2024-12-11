from rest_framework import viewsets
from Notifications.models import Notification
from Notifications.serializers import NotificationSerializer


# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
