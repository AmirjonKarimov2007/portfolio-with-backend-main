from django.shortcuts import render, redirect
from .models import HomeDefault, Skill, SocialMarkets, Statics, Company

def redirect_to_defaults(request):
    """Redirect to the defaults home page."""
    return redirect('defaults:home')  # Ensure 'home' is the name for the defaults view in urls.py

def defaults(request):
    """Render the default home page with all necessary context data."""
    home_defaults = HomeDefault.objects.all()
    skills = Skill.objects.all()
    social_markets = SocialMarkets.objects.all()
    statistics = Statics.objects.all()
    companies = Company.objects.all()
    print(home_defaults)
    data = {
        "home_defaults": home_defaults,
        "skills": skills,
        "social_markets": social_markets,
        "statistics": statistics,
        "companies": companies
    }
    
    return render(request, 'index.html', context=data)

def about(request):
    """Render the about page."""
    return render(request, 'about.html')

def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html')
