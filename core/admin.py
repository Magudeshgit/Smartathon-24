from django.contrib import admin
from .models import statements, events, registrations, hackathonreg

# Register your models here.
admin.site.register([statements, events, registrations, hackathonreg])
admin.site.site_header = "Smartathon'24"
admin.site.site_title = "Smartathon'24"

