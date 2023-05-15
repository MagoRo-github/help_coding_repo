from django.contrib import admin

from .models import Homepage

# admin.site.register(Homepage)
@admin.register(Homepage)
class SetAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('code',)}
    list_display = ('code', 'tipo')
