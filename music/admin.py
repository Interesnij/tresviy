from django.contrib import admin
from .models import SoundParsing


class SoundParsingAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    class Meta:
            model = SoundParsing


admin.site.register(SoundParsing, SoundParsingAdmin)
