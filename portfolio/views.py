from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Service,Project
# Create your views here.
from defaults.models import HomeDefault, Skill, SocialMarkets, Statics, Company
import uuid
from django.shortcuts import redirect, get_object_or_404
from .models import Post, Like
from .utils import check_click_likes



class HomePageView(ListView):
    model = Service
    template_name = 'index.html'
    context_object_name = 'object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = HomeDefault.objects.all()
        project = Project.objects.all() 
        # Fetching data from the defaults app
        context['home_defaults'] = home
        context['skills'] = Skill.objects.all()
        context['social_markets'] = SocialMarkets.objects.all()
        context['statistics'] = Statics.objects.all()
        context['companies'] = Company.objects.all()
        context['projects'] = project
     
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

from .models import Post,Category,BlogTag,Comment,Like


# Blog Sahifasi
# Blog Sahifasi
# Blog Sahifasi


def rightblogview(request):
    user_id = assign_user_id(request)
    categories = Category.objects.all().order_by('?')[:4]
    posts = Post.objects.all()
    related_posts = Post.objects.all()
    return render(request,'blog-list-sidebar-right.html',context=
    {'posts': posts, 
     'user_id': user_id,
     "categories":categories,
     "related_posts":related_posts
     }
     )


def assign_user_id(request):
    if not request.session.get('user_id'):
        request.session['user_id'] = str(uuid.uuid4())
    
    return request.session['user_id']

def likes_view(request, user_id, pk):
    post = get_object_or_404(Post, id=pk)
    
    # Ensure the session is modified
    request.session.modified = True
    
    # Retrieve list of post IDs that the user has liked
    liked_posts = check_click_likes(request)
    
    if post.pk in liked_posts:
        # Remove the like if the post was already liked
        liked_posts.remove(post.pk)
        Like.objects.filter(post=post, user_id=user_id).delete()
    else:
        # Add the like if the post was not liked before
        liked_posts.append(post.pk)
        Like.objects.create(post=post, user_id=user_id)
    
    return redirect('blog')

def category_list(request,category_slug):
    slug = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=slug)
    categories = Category.objects.exclude(slug__in=[category_slug]).order_by('?')[:4]
    related_posts = Post.objects.filter(category=slug)

    return render(request,'blog-list-sidebar-right.html',context={
        "slug":slug,
        "posts":posts,
        "categories":categories,
        "related_posts":related_posts,
        })


# Search Deatils

def search(request):
    related_posts = Post.objects.all().order_by('?')[:10]
    categories = Category.objects.all().order_by('?')[:4]
    query = request.GET.get('query')
    posts = Post.objects.filter(title__icontains=query)
    return render(request,"blog-list-sidebar-right.html",context={"related_posts":related_posts,"posts":posts,"categories":categories})