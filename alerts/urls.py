from django.urls import path, include
from rest_framework import routers
from .views import SendReportViewSet, EcoContributionViewSet
router = routers.DefaultRouter()
router.register(r'send-report', SendReportViewSet)
router.register(r'contribute', EcoContributionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
