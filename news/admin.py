from django.contrib import admin
from .models import NewsArticle, Event

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'is_published']
    list_filter = ['is_published']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_active']