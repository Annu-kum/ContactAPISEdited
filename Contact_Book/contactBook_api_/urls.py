from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
      path('getContact/', views.GetViewset.as_view(),name='getcontact'),
      path('postContact/',views.Postcontactviews.as_view(),name='createcontact'),
      path('delete/<str:name>/',views.deletecontactviews.as_view(),name='deletecontact'),
      path('update/<str:Name>/',views.updatecontactviews.as_view(),name='updatecontact'),

]