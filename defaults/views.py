from django.views.generic import ListView
from .models import Defaults

class DefaultDetails(ListView):
    template_name = 'project-details.html'
    model = Defaults
    context_object_name = 'defaults'  # Shablondagi o'zgaruvchi nomi
