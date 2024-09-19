from django.db import models

# Create your models here.



    
class HomeDefault(models.Model):
    name = models.CharField(max_length=200,verbose_name="ism familiya")
    title = models.CharField(verbose_name="Sayt sarlavhasi",max_length=300)
    logo = models.ImageField(verbose_name="logo")
    avatar = models.ImageField(verbose_name="Avatar rasmi")
    video_link = models.CharField(max_length=300,verbose_name="Video linki")
    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200,verbose_name="Nomi")
    number = models.IntegerField(verbose_name="Foiz")
    skill = models.ForeignKey(HomeDefault,on_delete=models.PROTECT,related_name='defaults')
    def __str__(self) -> str:
        return self.title

class SocialMarkets(models.Model):
    linkedin = models.CharField(max_length=400,verbose_name="Linkedin",blank=True)
    instagram = models.CharField(max_length=400,verbose_name="Instagram",blank=True)
    telegram = models.CharField(max_length=400,verbose_name="Telegram",blank=True)
    facebook = models.CharField(max_length=400,verbose_name="Facebook",blank=True)
    youtube = models.CharField(max_length=400,verbose_name="Youtube",blank=True)
    fiverr = models.CharField(max_length=400,verbose_name="Fiverr",blank=True)
    upwork = models.CharField(max_length=400,verbose_name="Upwork",blank=True)
    phone_number = models.CharField(max_length=400,verbose_name="Telefon Raqam",blank=True)
    email_address = models.CharField(max_length=400,verbose_name="email manzil")
    social = models.ForeignKey(HomeDefault, on_delete=models.CASCADE, related_name='socials')
    def __str__(self) -> str:
        return self.phone_number

class Static(models.Model):
    resume = models.FileField(verbose_name="resume")
    happy_clients = models.IntegerField(verbose_name="Hursand Mijozlar")
    project_complate = models.IntegerField(verbose_name="Muvaffaqiyatli loyihalar")
    experience = models.IntegerField(verbose_name="Tajriba")
    static = models.ForeignKey(HomeDefault,on_delete=models.PROTECT,related_name="statics")
    def __str__(self) -> str:
        return self.happy_clients
    


class Company(models.Model):
    name = models.CharField(max_length=200,verbose_name="Kampaniya nomi")
    logo = models.ImageField(verbose_name="Kampaniya logo",null=True,blank=True)
    company = models.ForeignKey(HomeDefault,on_delete=models.PROTECT,related_name="companies")
    def __str__(self) -> str:
        return self.name