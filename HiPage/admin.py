from django.contrib import admin
from django import forms
from HiPage.models import event, heroe, date, place, army, User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(event, EventAdmin)
admin.site.register(army, ArmyAdmin)
admin.site.register(heroe, HeroeAdmin)
