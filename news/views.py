from django.views.generic import ListView, DetailView
from .models import NewsArticle, Event

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news/news_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return NewsArticle.objects.filter(is_published=True)

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

class EventListView(ListView):
    model = Event
    template_name = 'news/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(is_active=True)