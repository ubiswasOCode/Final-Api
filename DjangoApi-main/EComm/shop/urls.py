
from shop import views
from django.urls import path
from Ecommapp.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)


urlpatterns = [

    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('Updateuser/<str:id>/', views.Updateuser, name='Updateuser'),
    path('getuser/', views.getuser, name='getuser'),

    path('proShow/', views.proShow, name='proShow'),
    path('CreatePro/', views.CreatePro, name='CreatePro'),
    path('UpdatePro/<str:id>/', views.UpdatePro, name='UpdatePro'),
    path('DelPro/', views.DelPro, name='DelPro'),

    path('CreateCate/', views.CreateCate, name='CreateCate'),
    path('showCate/', views.showCate, name='showCate'),
    path('DelCategory/', views.DelCategory, name='DelCategory'),
    path('updateCate/<str:id>/', views.updateCate, name='updateCate'),

    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
]
