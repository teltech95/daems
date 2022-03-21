from rest_framework import serializers
from .models import SendReport, EcoContribution


class SendReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendReport
        fields = '__all__'

class EcoContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EcoContribution
        fields = '__all__'
