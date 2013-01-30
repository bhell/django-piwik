from django.contrib import admin
from piwik.models import Analytics


class AnalyticsAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)

admin.site.register(Analytics, AnalyticsAdmin)
