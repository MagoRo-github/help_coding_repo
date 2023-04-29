from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Homepage

class HomepageView(TemplateView):
    template_name = "homepage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codici'] = Homepage.objects.all()
        context['nav'] = Homepage.objects.all()
        return context
    
