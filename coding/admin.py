from django.contrib import admin

from .models import Coding

@admin.register(Coding)
class SetAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('linguaggio',), 'slug_argomento': ('argomento',)}
    # prepopulated_fields={'slug_argomento': ('argomento',)}