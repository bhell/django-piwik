from django.contrib import admin
from piwik.models import Analytics, Settings

class SettingsInline(admin.TabularInline):
    model = Settings
    extra = 5

class AnalyticsAdmin(admin.ModelAdmin):
    readonly_fields = ('preview',)
    inlines = [SettingsInline,]

admin.site.register(Analytics, AnalyticsAdmin)
