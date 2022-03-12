
from rest_framework import viewsets
from .serializers import DisasterAlertsSerializer
from .models import DisasterAlerts


class DisasterAlertsViewSet(viewsets.ModelViewSet):

    serializer_class = DisasterAlertsSerializer
    queryset = DisasterAlerts.objects.all()
