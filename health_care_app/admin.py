from django.contrib import admin

from health_care_app.models import Patients


class PatientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'gender', 'created_at']
    search_fields = ['id', 'name', 'phone', 'email', 'gender']
    list_filter = ['gender']
    list_per_page = 8


admin.site.register(Patients, PatientsAdmin)


# Support calls
class CallAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display = ['user', 'reason', 'option', 'created_at', 'status', '_']
    search_fields = ['user', 'reason', 'option']
    list_per_page = 8
