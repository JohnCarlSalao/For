from django.contrib.auth.models import User
from rest_framework import serializers

from portfolio.models.portfolio_model import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = '__all__'