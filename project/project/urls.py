from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupPage, name="signupPage"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('adminPage/', views.adminPage, name="adminPage"),
    path('myProfilePage/', views.myProfilePage, name="myProfilePage"),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
