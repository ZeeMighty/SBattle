from django.contrib import admin
from mains.models import event, heroe

class Heroes(admin.TabularInline):
    model = heroe
    extra = 1

class EventAdmin(admin.ModelAdmin):
    model = event
    list_display = ('title', 'date')
    list_filter = ['id']
    search_fields = ['title']
    fieldsets = [
    ('Title', {'fields': ['title']}),
    ('History', {'fields': ['body']}),
    ('Date', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [Heroes]

admin.site.register(event, EventAdmin)
