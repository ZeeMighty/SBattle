from django.contrib import admin
from mains.models import event, heroe, date

class Heroes(admin.TabularInline):
    model = heroe
    extra = 1

class date(admin.TabularInline):
    model = date
    extra = 1

class EventAdmin(admin.ModelAdmin):
    model = event
#    list_display = ('title')
    list_filter = ['id']
    search_fields = ['title']
    fieldsets = [
    ('Title', {'fields': ['title']}),
    ('History', {'fields': ['body'], 'classes': ['collapse']}),
    ('Result', {'fields': ['result'], 'classes': ['collapse']}),
    ]
    inlines = [Heroes, date]

admin.site.register(event, EventAdmin)
