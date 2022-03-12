from django.urls import path, include
from rest_framework import routers
from .views import DisasterAlertsViewSet
router = routers.DefaultRouter()
router.register(r'alerts', DisasterAlertsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
