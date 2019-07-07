from django.contrib import admin
from gallery.models import Images, Settings


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'created')
    search_fields = ('name', 'tags', 'created')


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('display', 'number_displayed', 'method', 'interval_for_slideshow', 'created')
    search_fields = ('created',)


admin.site.register(Images, ImagesAdmin)
admin.site.register(Settings, SettingsAdmin)