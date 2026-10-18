from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'age_range', 'order']
    list_filter = ['level', 'is_boarding_available']
    prepopulated_fields = {'slug': ('name',)}