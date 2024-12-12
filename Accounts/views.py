from wsgiref import headers

from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all().order_by('id')
        serializer_class = UserSerializer
        permission_classes = [permissions.AllowAny]
        def create(self, request, *args, **kwargs):
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                password = request.data['password']
                user.set_password(password)
                user.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)


