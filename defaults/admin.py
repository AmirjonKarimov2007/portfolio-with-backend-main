from django.contrib import admin
from .models import HomeDefault, Skill, SocialMarkets, Statics, Company

@admin.register(HomeDefault)
class HomeDefaultAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'skill')
    search_fields = ('title',)
    
@admin.register(SocialMarkets)
class SocialMarketsAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'linkedin', 'instagram', 'telegram', 'facebook', 'youtube', 'fiverr', 'upwork', 'phone_number')
    search_fields = ('email_address', 'linkedin', 'instagram')

@admin.register(Statics)
class StaticAdmin(admin.ModelAdmin):
    list_display = ( 'happy_clients', 'project_complate', 'experience')
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

