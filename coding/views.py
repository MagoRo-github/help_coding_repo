from django.shortcuts import render

from django.views.generic import DetailView, ListView
from homepage.models import Homepage

from .models import Coding

class CodingDetailView(DetailView):
    model = Coding
    template_name = "coding/coding_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CodingListView(ListView):
    model = Coding
    template_name = "coding/coding_list.html"

    def get_queryset(self):
        queryset = self.request.GET.get('q')
        if queryset:
            return Coding.objects.filter(linguaggio=queryset)
            # sono stati inseriti due filtri che ricercano per codice e per name (la ricerca restituirà risultati per entrambi i filtri
        else:
            return 

    def get_context_data(self, **kwargs):
        lin = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        try:
            context['linguaggio'] = Coding.objects.filter(linguaggio=lin)[0]
        except:
            context['linguaggio'] = ''
        context['nav'] = Homepage.objects.all()
 
        return context

    