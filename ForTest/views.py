from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class TestMenuView(TemplateView):
    template_name = "ForTest/menu.html"
    
    def get_context_data(self, **kwargs):
        context = super(TestMenuView, self).get_context_data(**kwargs)
        context['hello'] = 'hello'
        return context