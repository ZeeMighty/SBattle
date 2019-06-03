from django.contrib import admin
from mains.models import event, heroe, date, place, army

class Heroes(admin.TabularInline):
    model = heroe
    extra = 1

class Date(admin.TabularInline):
    model = date
    extra = 1

class Place(admin.TabularInline):
    model = place
    extra = 1

class Army(admin.TabularInline):
    model = army
    extra = 1

class HeroeAdmin(admin.ModelAdmin):
    model = heroe
    list_filter = ['id']
    search_fields = ['name']
    fieldsets = [
    ('Name', {'fields': ['name']}),
    ('Bio', {'fields': ['biography']}),
    ('Army', {'fields': ['army']}),
    ('Rewards', {'fields': ['rewards']}),
    ('Lived', {'fields': ['lived']}),
    ]

class ArmyAdmin(admin.ModelAdmin):
    model = army
    list_filter = ['id']
    search_fields = ['name']
    inlines = [Heroes]


class EventAdmin(admin.ModelAdmin):
    model = event
#    list_display = ('title')
    list_filter = ['id']
    search_fields = ['title']
    fieldsets = [
    ('Title', {'fields': ['title']}),
    ('Participants', {'fields': ['participants']}),
    ('History', {'fields': ['body'], 'classes': ['collapse']}),
    ('Result', {'fields': ['result'], 'classes': ['collapse']}),
    ]
    inlines = [Date, Place]

admin.site.register(event, EventAdmin)
admin.site.register(army, ArmyAdmin)
admin.site.register(heroe, HeroeAdmin)
