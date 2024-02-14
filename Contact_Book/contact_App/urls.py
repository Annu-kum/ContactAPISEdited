from django.urls import path,include
from .views import UserViewsets

from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()

router.register(r'Users',UserViewsets)

urlpatterns = [
    path('',include(router.urls)),
  
]