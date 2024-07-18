from django.shortcuts import render
from rest_framework import generics
from api.serializers import QueryHistorySerializer
from api.models import Statistic
from collections import Counter

# Create your views here.
class StaticticApiView(generics.ListAPIView):
    serializer_class = QueryHistorySerializer
    queryset = Statistic.objects.all()