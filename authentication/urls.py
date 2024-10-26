from django.urls import path
from .views import login_view,forgotpassword,signup,logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', forgotpassword, name='forgotpassword'),
    path('logout/', logout_view, name='logout')

]
