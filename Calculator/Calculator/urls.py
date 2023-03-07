"""Calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Task_Executor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('signins',views.logins_page),
    path('signinm',views.loginm_page),
    path('signups',views.signups_page),
    path('signupm',views.signupm_page),
    path('test',views.take_test),
    path('addq',views.question),
    path('<int:qno>/<str:question>', views.answer)
]
