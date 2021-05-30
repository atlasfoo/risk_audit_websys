from django.contrib import admin

from controls.models import Control


class ControlAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Media:
        css = {
            'all': ('vendor/css/custom_ckeditor.css',)
        }


admin.site.register(Control, ControlAdmin)
