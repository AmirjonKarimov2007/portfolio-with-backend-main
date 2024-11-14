from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.
from defaults.models import HomeDefault, Skill, SocialMarkets, Statics, Company
import uuid
from django.shortcuts import get_object_or_404
from .models import Post, Like,Service,Project,Profile,Education
from .utils import check_click_likes
from django.core.paginator import Paginator


class HomePageView(ListView):
    model = Service
    template_name = 'index.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(id=1)
        home = HomeDefault.objects.all()
        project = Project.objects.all() 
        # Fetching data from the defaults app
        context['home_defaults'] = home
        context['skills'] = Skill.objects.all()
        context['social'] = SocialMarkets.objects.get(id=1)
        context['statistics'] = Statics.objects.all()
        context['companies'] = Company.objects.all()
        context['projects'] = project
        context['posts'] = Post.objects.all()[:4]
        context['profile'] = profile
     
        return context
    
# About Page View
def aboutpageview(request):
    home = HomeDefault.objects.all()
    defaults = HomeDefault.objects.get(id=1)
    statistics = Statics.objects.all()
    social = SocialMarkets.objects.get(id=1)
    profile = Profile.objects.get(id=1)
    data = {
        'statistics':statistics,
        'home_defaults':home,
        'defaults':defaults,
        'social':social,
        'profile':profile
    }
    return render(request,'about.html',data)


# Services List
class ServicePageView(ListView):
    template_name = 'service-list.html'
    model = Service
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = HomeDefault.objects.all()
        project = Project.objects.all() 
        # Fetching data from the defaults app
        context['home_defaults'] = home
        context['skills'] = Skill.objects.all()
        context['social'] = SocialMarkets.objects.get(id=1)
        context['statistics'] = Statics.objects.all()
        context['companies'] = Company.objects.all()
        context['projects'] = project
        return context


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
        context['social'] = SocialMarkets.objects.get(id=1)
        context['home_defaults'] =  HomeDefault.objects.all()
        context['object_list'] = Service.objects.all()[:4]  # Limit to first four services
        
        # Preprocess plans_text to replace commas followed by space with <br> tags
        
        return context
    

class ProjectPageView(ListView):
    template_name = 'project-list.html'
    model = Project
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social'] = SocialMarkets.objects.get(id=1)
        context['home_defaults'] =  HomeDefault.objects.all()
        context['statistics'] = Statics.objects.all()

        return context

class ProjectDetailsView(DetailView):
    template_name = 'project-details.html'
    model = Project
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social'] = SocialMarkets.objects.get(id=1)
        context['home_defaults'] =  HomeDefault.objects.all()
        context['statistics'] = Statics.objects.all()

        return context

from .models import Post,Category,BlogTag,Comment,Like


# Blog Sahifasi
# Blog Sahifasi
# Blog Sahifasi


def rightblogview(request):
    user_id = assign_user_id(request)
    categories = Category.objects.all().order_by('?')[:4]
    posts = Post.objects.all().order_by('-publish_date')  # Order by the desired field
    related_posts = Post.objects.all()
    paginator = Paginator(posts,8)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    
    return render(request,'blog-list-sidebar-right.html',context=
    {'posts': page_obj, 
     'user_id': user_id,
     "categories":categories,
     "related_posts":related_posts,
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
    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)

    return render(request,'blog-list-sidebar-right.html',context={
        "slug":slug,
        "posts":page_obj,
        "categories":categories,
        "related_posts":related_posts,
        })


# Search Deatils

def search(request):
    related_posts = Post.objects.all().order_by('?')[:10]
    categories = Category.objects.all().order_by('?')[:4]
    query = request.GET.get('query')
    posts = Post.objects.filter(title__icontains=query)
    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    return render(request,"blog-list-sidebar-right.html",context={"related_posts":related_posts,"posts":page_obj,"categories":categories})






# BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE
# BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE
# BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE
# BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE
# BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE # BLOG DETAILS PAGE
from .utils import check_read_articles
def blogdetailsview(request,pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all().order_by('?')[:4]
    social_media = SocialMarkets.objects.all()
    request.session.modified = True
    if post.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(post.id)
        post.views +=1
        post.save()


    if request.method == "POST":
        name = request.POST.get('name')
        jobtitle = request.POST.get('job')
        comment = request.POST.get('comment')
        image = 'https://amirjonkarimov2007.github.io/portfolio/assets/images/users/user-1.jpg'
        if all([name,jobtitle,comment]):
            Comment.objects.create(
                author = name,
                jobtitle = jobtitle,
                comment = comment,
                post = post,
                image = image
            )
    related_posts = Post.objects.filter(category=post.category).exclude(id__in=[0,post.id]).order_by('?')[:5]

    data = {
        "post":post,
        "categories":categories,
        "social_media":social_media,
        "related_posts":related_posts
        
    }

    return render(request,'blog-details-sidebar-right.html',data)
from django import forms
import asyncio
from django.shortcuts import render, redirect
from .forms import  ContactForm
# Telegram bot tokeni va admin chat ID sini kiriting
import requests

TELEGRAM_BOT_TOKEN = '6679509079:AAF8mJpLY_LBIXiHO9uLkGFBJ27fQe5pj3w'
ADMIN_CHAT_ID = '1612270615'

def send_message_to_admin(form_data):
    message = (
        f"*Yangi kontakt formasi yuborildi!*\n\n"
        f"*Ism:* {form_data['name']}\n"
        f"*Email:* {form_data['email']}\n"
        f"*Telefon:* {form_data['phone']}\n"
        f"*Mavzu:* {form_data['subject']}\n"
        f"*Xabar:* {form_data['message']}"
    )

    # Clean the phone number
    phone_number = form_data['phone'].replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if not phone_number.startswith("+"):
        phone_number = "+998" + phone_number  # Adjust to your country's code

    # Create the button URL
    contact_url = f"t.me/{phone_number}"

    # Create the button
    contact_btn = {
        "inline_keyboard": [[{"text": "📞 Bog'lanish", "url": contact_url}]]
    }

    # Send the message via Telegram API
    response = requests.post(
        f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
        json={
            "chat_id": ADMIN_CHAT_ID,
            "text": message,
            "parse_mode": 'Markdown',
            "reply_markup": contact_btn
        }
    )

    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")

def contactpageview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form.save()
            send_message_to_admin(form_data)
            return redirect('/')

    else:
        form = ContactForm()

    informations = SocialMarkets.objects.get(id=1)
    social = SocialMarkets.objects.get(id=1)
    data = {
        'informations': informations,
        'social': social,
        'form': form,
    }
    return render(request, 'contact.html', data)