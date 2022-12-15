
from django.urls import include, path
from rest_framework import routers



from .. import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename= 'Register')
router.register(r'education', views.EducationViewSet, basename = 'Education')
router.register(r'work', views.WorkViewSet, basename ='Work' ) 
router.register (r'portfolio', views.PortfolioViewSet , basename= 'Portfolio')


urlpatterns_router = [path ('', include (router.urls)),

]