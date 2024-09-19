from django.urls import path
from .views import redirect_to_defaults, defaults

app_name = 'defaults'

urlpatterns = [
    path('', redirect_to_defaults, name='redirect'),  # Asosiy URL redirekt qiladi
    path('home/', defaults, name='home'),  # Asosiy sahifa
]
