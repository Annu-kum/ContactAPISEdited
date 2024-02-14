from django.urls import path,include
from .views import ContactViewset

from rest_framework import routers
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()

router.register(r'contactBook',ContactViewset)

urlpatterns = [
    path('',include(router.urls)),
   

  
]