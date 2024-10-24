from django.urls import path
from .views import login,forgotpassword

urlpatterns = [
    path('login/', login, name='login'),
    path('forgot-password/', forgotpassword, name='forgotpassword'),
]
