from django.urls import path
from .views import HomePageView,ServicePageView,ServiceDetailsView,ProjectPageView,ProjectDetailsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services', ServicePageView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceDetailsView.as_view(), name='service_details'),
    path('projects', ProjectPageView.as_view(), name='projects'),
    path('project/<int:pk>/',ProjectDetailsView.as_view(),name='project-detail')
]