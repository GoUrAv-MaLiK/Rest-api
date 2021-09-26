"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from SerializerRelation.views import SongView,SingerView
from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers
import rest_framework
from rest_framework.routers import DefaultRouter
from SessionAuhtentication import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView
#to get token from http request
# for ##TokenAuthentication# install httpie and write http POST {url} username={username} password="password" 
router=DefaultRouter()
router.register('student',views.student_info)
# router.register('singer/',SingerView,basename='singer')
# router.register('song/',SongView,basename='song')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('filter/',views.student_info.as_view()),
    # path('pagination/',views.student_info.as_view()),
    # path('song/',SongView.as_view()),
    # path('singer/',SingerView.as_view()),
    path('',include('rest_framework.urls',namespace='rest_framework')),
    #simpleJWT code
# """ path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
#     path('refreshtoken/',TokenRefreshView.as_view(),name='token_refrsh'),
#     path('verifytoken/',TokenVerifyView.as_view(),name='token_verify') """
]
