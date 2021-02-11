from django.contrib import admin
from .models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_filter=["name","paradigm"]
    list_display=["name","paradigm"]