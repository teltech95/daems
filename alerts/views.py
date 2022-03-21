
from rest_framework import viewsets
from .serializers import SendReportSerializer, EcoContributionSerializer
from .models import SendReport, EcoContribution


class SendReportViewSet(viewsets.ModelViewSet):

    serializer_class = SendReportSerializer
    queryset = SendReport.objects.all()

class EcoContributionViewSet(viewsets.ModelViewSet):

    serializer_class = EcoContributionSerializer
    queryset = EcoContribution.objects.all()
