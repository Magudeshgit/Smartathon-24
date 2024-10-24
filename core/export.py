from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from .models import registrations, events

class Registrationexp(resources.ModelResource):
    eventname = Field(
        attribute='event',
        widget = ForeignKeyWidget(events, 'name')
    )
    class Meta:
        model = registrations