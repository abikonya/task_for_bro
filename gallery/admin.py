from django.contrib import admin
from gallery.models import Images


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'created')
    search_fields = ('name', 'tags', 'created')


admin.site.register(Images, ImagesAdmin)