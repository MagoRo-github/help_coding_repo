from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Homepage

class HomepageView(TemplateView):
    template_name = "homepage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_coding'] = Homepage.objects.all()

        context['codici'] = Homepage.objects.filter(tipo='LN')
        context['nav'] = Homepage.objects.filter(tipo='LN')

        context['utili'] = Homepage.objects.filter(tipo='UT')
        context['utili_NAV'] = Homepage.objects.filter(tipo='UT')
        return context
    
