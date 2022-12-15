from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.education_model import Education

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields ='__all__'