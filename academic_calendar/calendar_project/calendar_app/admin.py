from django.contrib import admin
from .models import Calendar, Event

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calendar', 'start_date', 'end_date')
