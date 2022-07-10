from django.contrib import admin

# Register your models here.
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('key', 'created_at',)

admin.site.register(Report, ReportAdmin)
