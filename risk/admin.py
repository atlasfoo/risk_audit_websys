from django.contrib import admin

from risk.models import Risk


class RiskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Media:
        css = {
            'all': ('vendor/css/custom_ckeditor.css',)
        }


admin.site.register(Risk, RiskAdmin)
