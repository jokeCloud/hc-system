from django.contrib import admin

from health_care_app.models import Patients


class PatientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'gender', 'created_at']
    search_fields = ['id', 'name', 'phone', 'email', 'gender']
    list_per_page = 8


admin.site.register(Patients, PatientsAdmin)
