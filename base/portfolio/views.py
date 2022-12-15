
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers.UserSerializers import UserSerializer
from .serializers.EducationSerializers import EducationSerializer
from .serializers.PortfolioSerializers import PortfolioSerializer
from .serializers.WorkSerializers import WorkSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models.education_model import *
from .models.portfolio_model import *
from .models.work_model import *

class UserViewSet(viewsets.ModelViewSet):

   queryset = User.objects.all().order_by('-date_joined')
   serializer_class = UserSerializer
   permission_classes = [permissions.AllowAny]


class EducationViewSet(viewsets.ModelViewSet):
   queryset = Education.objects.all()
   serializer_class = EducationSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]

class WorkViewSet(viewsets.ModelViewSet):
   queryset = Work.objects.all()
   serializer_class = WorkSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]
class PortfolioViewSet(viewsets.ModelViewSet):
   queryset = Portfolio.objects.all()
   serializer_class = PortfolioSerializer 
   permission_classes = [IsAuthenticatedOrReadOnly]

