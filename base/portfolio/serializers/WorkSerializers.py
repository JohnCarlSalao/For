from django.contrib.auth.models import User
from rest_framework import serializers

from portfolio.models.work_model import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
    