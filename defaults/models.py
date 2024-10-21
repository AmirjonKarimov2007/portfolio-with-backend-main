from django.db import models

# Create your models here.



    
class HomeDefault(models.Model):
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
    github = models.CharField(max_length=400,verbose_name="Github")
    youtube = models.CharField(max_length=400,verbose_name="Youtube",blank=True)
    fiverr = models.CharField(max_length=400,verbose_name="Fiverr",blank=True)
    upwork = models.CharField(max_length=400,verbose_name="Upwork",blank=True)
    phone_number = models.CharField(max_length=400,verbose_name="Telefon Raqam",blank=True)
    email_address = models.CharField(max_length=400,verbose_name="email manzil")
    social = models.ForeignKey(HomeDefault, on_delete=models.CASCADE, related_name='socials')

    def __str__(self) -> str:
        return self.linkedin

class Statics(models.Model):
    happy_clients = models.BigIntegerField(verbose_name="Hursand Mijozlar")
    project_complate = models.BigIntegerField(verbose_name="Muvaffaqiyatli loyihalar")
    experience = models.BigIntegerField(verbose_name="Tajriba")
    def __str__(self) -> str:
        return str(self.happy_clients)
    


class Company(models.Model):
    name = models.CharField(max_length=200,verbose_name="Kampaniya nomi")
    logo = models.ImageField(verbose_name="Kampaniya logo",null=True,blank=True)
    company = models.ForeignKey(HomeDefault,on_delete=models.PROTECT,related_name="companies")
    def __str__(self) -> str:
        return self.name

