from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('participations',views.ParticipationViewSet)

urlpatterns =[
    path('',include(router.urls)),
]