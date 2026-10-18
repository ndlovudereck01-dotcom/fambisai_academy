from django.views.generic import ListView, DetailView
from django.core.cache import cache
from .models import Program

class ProgramListView(ListView):
    model = Program
    template_name = 'academics/program_list.html'
    context_object_name = 'programs'

    def get_queryset(self):
        cached = cache.get('all_programs')
        if cached is None:
            cached = list(Program.objects.all())
            cache.set('all_programs', cached, 600)
        return cached

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'academics/program_detail.html'
    context_object_name = 'program'
    slug_url_kwarg = 'slug'