from django import views
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'useradmin', views.AdminViewSet, basename='admin')
router.register(r'register', views.RegisterView, basename='auth_register')
router.register(r'user', views.NUserViewSet, basename='user')
router.register(r'uploud', views.csvfileViewSet, basename='uploud')

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),

    # path('', views.Home, name='home'),
    # path('', views.Home2, name='index2'),
    # path('datatable', views.datatable, name="datatable"),
    path('',include(router.urls)),
    path('login',views.Cpage,name="Cpage"),
    path('logout',views.Dec,name="Dec"),
    path('',views.indexf, name='indexf'),
    path('dash',views.send_files,name="dash"),
    path('rapport',views.search,name="rapport"),
    path('upload',views.upload,name="upload"),
    path('decode/',views.verify_token,name="decode"),


]

