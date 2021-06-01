from django.contrib import admin

from incidences.models import Incidence


class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

    class Media:
        css = {
            'all': ('vendor/css/custom_ckeditor.css',)
        }


admin.site.register(Incidence, IncidencesAdmin)
