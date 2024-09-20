from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Service,Project
# Create your views here.
from defaults.models import HomeDefault, Skill, SocialMarkets, Statics, Company

class HomePageView(ListView):
    model = Service
    template_name = 'index.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = HomeDefault.objects.all()
        
        # Fetching data from the defaults app
        context['home_defaults'] = home
        context['skills'] = Skill.objects.all()
        context['social_markets'] = SocialMarkets.objects.all()
        context['statistics'] = Statics.objects.all()
        context['companies'] = Company.objects.all()
        return context
# Services List
class ServicePageView(ListView):
    template_name = 'service-list.html'
    model = Service


class ServiceDetailsView(DetailView):
    template_name = 'service-details.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        
        # Add related service plans to the context
        context['basic_service'] = service.basic_service
        context['standard_service'] = service.standard_service
        context['premium_service'] = service.premium_service
        context['object_list'] = Service.objects.all()[:4]  # Limit to first four services
        
        # Preprocess plans_text to replace commas followed by space with <br> tags
        
        return context
    

class ProjectPageView(ListView):
    template_name = 'project-list.html'
    model = Project


class ProjectDetailsView(DetailView):
    template_name = 'project-details.html'
    model = Project