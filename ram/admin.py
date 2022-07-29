from django.contrib import admin
from .models import AllChars, Episodes


class AllCharsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'species', 'type', 'gender')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'status', 'species', 'gender')
    
admin.site.register(AllChars, AllCharsAdmin)
admin.site.register(Episodes)
# Register your models here.
