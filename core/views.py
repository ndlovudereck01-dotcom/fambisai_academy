from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.cache import cache
from .models import ContactMessage
from news.models import NewsArticle

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Cache latest news for 5 minutes
        latest_news = cache.get('home_latest_news')
        if latest_news is None:
            latest_news = list(NewsArticle.objects.filter(is_published=True).order_by('-published_at')[:3])
            cache.set('home_latest_news', latest_news, 300)
        context['latest_news'] = latest_news
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def post(self, request):
        from django.contrib import messages
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        if name and email and message_text:
            ContactMessage.objects.create(
                name=name, email=email,
                phone=request.POST.get('phone', ''),
                message=message_text
            )
            messages.success(request, 'Thank you. Your message has been received.')
        return render(request, 'core/contact.html')