from django import views
from django.contrib import admin
from django.urls import path
from health_care_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name='frontend'),
]
