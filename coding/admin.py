from django.contrib import admin

from .models import Coding

@admin.register(Coding)
class SetAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('linguaggio',)}