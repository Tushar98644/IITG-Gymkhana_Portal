from django.contrib import admin

from Backend.models import meeting
from Backend.models import ugSenator
from Backend.models import pgSenator
from Backend.models import facultyExecutivebodie
from Backend.models import studentExecutivebodie
from Backend.models import upcomingEvent
from Backend.models import upcomingEventlead



# Register your models here.
admin.site.register(meeting)
admin.site.register(ugSenator)
admin.site.register(pgSenator)
admin.site.register(facultyExecutivebodie)
admin.site.register(studentExecutivebodie)
admin.site.register(upcomingEvent)
admin.site.register(upcomingEventlead)