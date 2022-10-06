from django.contrib import admin
from django.urls import include, path
from health_care_app import views

urlpatterns = [
    # path to access the admin page
    path('admin/', admin.site.urls),
    # path to render homepage
    path('', views.frontend, name='frontend'),
    # path to login/logout
    path('login/', include('django.contrib.auth.urls')),

    # ================ #
    # BACKEND SECTION  #
    # ================ #
    # path to access the backend page
    path('backend/', views.backend, name='backend'),
    # path to add patient
    path('add_patient', views.add_patient, name='add_patient'),
]
