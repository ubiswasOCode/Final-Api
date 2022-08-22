
from . import views 
from django.urls import path
from Ecommapp.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
     TokenObtainPairView,
)


urlpatterns = [
    path('createuser',views.createuser,name='createuser'),
    path('getuser',views.getuser,name='getuser'),

    path('deleteuser/<str:pk>/',views.deleteUser,name='deleteuser'),
    path('updateuser/<str:pk>/',views.updateuser,name='updateuser'),

    path('createproduct/',views.createproduct,name='createproduct'),
    path('getproduct/',views.getproduct,name='getproduct'),
    path('updateproduct/<str:pk>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<str:pk>/',views.deleteproduct,name='deleteproduct'),

    path('createcategory/',views.createcategory,name='createcategory'),
    path('getcategory/',views.getcategory,name='getcategory'),
    path('deleteCategory/<str:pk>/',views.deleteCategory,name='deleteCategory'),
    path('updatecategory/<str:pk>/',views.updatecategory,name='updatecategory'),
   
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # path('',views.home,name='home'),
#     path('signin',views.signin,name='signin'),
#     path('signup',views.signup,name='signup'),
#     path('signout',views.signout,name='signout'),
]
