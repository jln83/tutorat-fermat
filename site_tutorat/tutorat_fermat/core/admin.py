from django.shortcuts import render
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cours

def home(request):
    return render(request, 'home.html')
from django.urls import path

#Custom User pour pouvoir ajouter un numero de telelphone
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'num_tel', 'is_active')
    search_fields = ('username', 'email', 'num_tel')
    ordering = ('username',)
    list_filter = ('is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('num_tel',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('num_tel',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Cours)