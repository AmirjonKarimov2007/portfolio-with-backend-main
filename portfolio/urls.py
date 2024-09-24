from django.urls import path
from .views import HomePageView,ServicePageView,ServiceDetailsView,ProjectPageView,ProjectDetailsView,rightblogview,likes_view,category_list
from .views import search
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services', ServicePageView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceDetailsView.as_view(), name='service_details'),
    path('projects', ProjectPageView.as_view(), name='projects'),
    path('project/<int:pk>/',ProjectDetailsView.as_view(),name='project-detail'),
    path('blog',rightblogview,name='blog'),
    path('like/<uuid:user_id>/<int:pk>/', likes_view, name='like_post'),
    path('<slug:category_slug>/posts/', category_list, name='category_list'),
    path('search/',search,name='search'),
    
]