from django.shortcuts import render

from django.views.generic import DetailView, ListView
from homepage.models import Homepage

from django.db.models import Q

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
            return Coding.objects.filter(Q(linguaggio=queryset))
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
        context['all_coding'] = Homepage.objects.all()
        context['nav'] = Homepage.objects.filter(tipo='LN')

 
        return context

class SearchCoding(ListView):
    model = Coding
    template_name = "coding/search_coding_list.html"

    def get_queryset(self):
        query_arg = self.request.GET.get('q_arg')
        query_lin = self.request.GET.get('q_ling')
        if not(query_lin):
            return Coding.objects.filter(Q(argomento__icontains=query_arg))
        elif query_arg:
            return Coding.objects.filter(Q(argomento__icontains=query_arg)) & Coding.objects.filter(Q(linguaggio=query_lin))
        else:
            return
        
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['all_coding'] = Homepage.objects.all()
 
        return context