from django.contrib import admin

from main.models import Issue


# admin.site.register(Issue)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['ref', 'complainant', 'status']


admin.site.site_header = 'HELPDESK Admin'
