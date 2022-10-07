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
    # path to delete patient
    path('delete_patient/<str:patient_id>',
         views.delete_patient, name='delete_patient'),
    # path to access the patients individually
    path('patient/<str:patient_id>', views.patient, name='patient'),
    # path to edit the patients
    path('edit_patient', views.edit_patient, name='edit_patient'),
]
