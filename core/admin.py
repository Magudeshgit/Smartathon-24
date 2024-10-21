from django.contrib import admin
from .models import statements, events, registrations, hackathonreg
from import_export.admin import ExportActionMixin

class RegistrationExport(ExportActionMixin, admin.ModelAdmin):
    pass

admin.site.register([statements, events, hackathonreg])
admin.site.register(registrations, RegistrationExport)
admin.site.site_header = "Smartathon'24"
admin.site.site_title = "Smartathon'24"

