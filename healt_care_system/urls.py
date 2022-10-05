from django.contrib import admin
from django.urls import include, path
from health_care_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name='frontend'),
    path('login/', include('django.contrib.auth.urls')),

    # ================ #
    # BACKEND SECTION  #
    # ================ #
    path('backend/', views.backend, name='backend'),
    path('add_patient', views.add_patient, name='add_patient'),
]
