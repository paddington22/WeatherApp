from rest_framework import serializers
from api.models import Statistic

class QueryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['city', 'count']