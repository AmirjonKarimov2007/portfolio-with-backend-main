from tabnanny import verbose

from django.db import models
from django.db.models import CharField
from django.core.exceptions import ValidationError
from django.utils import timezone

class FeaturesText(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class ServiceText(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField()
    def __str__(self):
        return self.title

class Planstext(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text[:50]

class Service(models.Model):
    title = models.CharField(max_length=100)
    photo = models.CharField(max_length=200, verbose_name='Rasm URL')
    features = models.ManyToManyField(FeaturesText, related_name='Xususiyatlar')
    subtitle = models.CharField(max_length=200, verbose_name="Sub Title")
    description = models.TextField(blank=True, null=True, verbose_name="Xizmat haqida")
    why_choose_me = models.TextField(blank=True, null=True, verbose_name='Nega aynan men')
    services_text = models.ManyToManyField(ServiceText, related_name='services', verbose_name="kichik qobiliyatlar")
    plans_text = models.TextField(blank=True, null=True, verbose_name="Tariflar haqida matn")
    def __str__(self):
        return self.title

class BasicService(models.Model):
    iid = models.IntegerField(default=1, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Basic", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='basic_service', null=True, blank=True)
    description = models.ManyToManyField(Planstext, verbose_name="Xizmat haqida - Basic")
    price = models.DecimalField(verbose_name="Basic package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Basic Service: {self.fullname}"

class StandardService(models.Model):
    iid = models.IntegerField(default=2, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Standard", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='standard_service', null=True, blank=True)
    description = models.ManyToManyField(Planstext, verbose_name="Xizmat haqida - Standard")
    price = models.DecimalField(verbose_name="Standard package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Standard Service: {self.fullname}"

class PremiumService(models.Model):
    iid = models.IntegerField(default=3, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Premium", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='premium_service', null=True, blank=True)
    description = models.ManyToManyField(Planstext, verbose_name="Xizmat haqida - Premium")
    price = models.DecimalField(verbose_name="Premium package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Premium Service: {self.fullname}"




class ProjectFilter(models.Model):
    title = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.title
class ProjectText(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='icons/')
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField(editable=True,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def split_text(self, chunk_size=330):
        return [self.text[i:i+chunk_size] for i in range(0, len(self.text), chunk_size)]

    
    
class ProjectPhoto(models.Model):
    photos = models.ImageField(upload_to='images/')
    def __str__(self) -> str:
        return self.photos.name

class Tag(models.Model):
    title = models.CharField(verbose_name="hashtag nomi:",max_length=200)
    def __str__(self) -> str:
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    optimal_text = models.ManyToManyField(ProjectText,editable=True, verbose_name="Hoqishiy tekslar")
    description = models.TextField(blank=True, null=True, verbose_name="Xizmat haqida")
    hashtag = models.ManyToManyField(Tag)
    photo = models.ManyToManyField(ProjectPhoto)
    filter_name = models.ForeignKey(
        ProjectFilter,
        on_delete=models.CASCADE
    )
    project_name = models.CharField(max_length=100, null=True, blank=True)
    clients = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    date = models.DateField()

    footer_title = models.CharField(max_length=200,verbose_name="Pastdagi Sarlavha")
    footer_text = models.TextField(verbose_name="Pastdagi Text")
    
    

    def __str__(self):
        return self.title

    def split_description(self, chunk_size=330):
        return [self.description[i:i+chunk_size] for i in range(0, len(self.description), chunk_size)]
    def split_footer_text(self, chunk_size=330):
        return [self.footer_text[i:i+chunk_size] for i in range(0, len(self.footer_text), chunk_size)]




# Blog Model
class Category(models.Model):
    name = models.CharField(verbose_name="Category name",max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    def __str__(self):
        return str(self.name)

class BlogTag(models.Model):
    name = models.CharField(verbose_name="Tag name",max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    def __str__(self):
        return str(self.name)
from django.db import models
from django.contrib.auth.models import User
# POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST
# POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST
# POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST
# POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST POST
class PostTag(models.Model):
    title = models.CharField(max_length=200,verbose_name="tag nomi")
    def __str__(self) -> CharField:
        return self.title
    
class Post(models.Model):
    title = models.CharField(verbose_name="Post title", max_length=550)
    description = models.TextField(verbose_name="Post Haqida")
    author = models.CharField(verbose_name="Post author", default="Admin", max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    tag = models.ManyToManyField(PostTag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    views = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(verbose_name="Published time", auto_now_add=True)
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=False)
    
    def split_description(self, chunk_size=330):
            return [self.description[i:i+chunk_size] for i in range(0, len(self.description), chunk_size)]
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-publish_date']

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user_id = models.CharField(verbose_name="post likes",max_length=500)
    
    def __str__(self):
        return str(self.user_id)

class Comment(models.Model):
    author = models.CharField(verbose_name="Comment author", max_length=100, blank=False)
    jobtitle = models.CharField(verbose_name="Job Title", max_length=200, blank=False)
    comment = models.TextField(verbose_name="Comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True)
    publish_date = models.DateTimeField(verbose_name="Published time", auto_now_add=True)


    def __str__(self):
        return str(self.author)

class Profile(models.Model):
    fullname = models.CharField(max_length=200,verbose_name="Ism Familiya")
    description = models.CharField(max_length=500,verbose_name='Siz haqingizda')
    job = models.CharField(max_length=200,verbose_name="Kasbingiz")
    age = models.IntegerField(verbose_name="Yosh",blank=True,null=True)
    logo = models.ImageField(upload_to='profile_logos/',blank=True,null=True)
    def __str__(self):
        return  self.fullname

# Education Model

class Education(models.Model):
    program_type = models.CharField(max_length=200,verbose_name="Yo'nalish")
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="educations")
    def clean(self):
        super().clean()
        today = timezone.now().date()

        if self.start_date > today:
            raise ValidationError('Start date cannot be in the past.')

        if self.end_date <= self.start_date:
            raise ValidationError('End date must be after the start date.')

    def __str__(self):
        return str(self.institution)

class Experience(models.Model):
    job = models.CharField(max_length=200, verbose_name="Kasb")
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")

    def clean(self):
        super().clean()
        today = timezone.now().date()

        if self.start_date > today:
            raise ValidationError('Start date cannot be in the past.')

        if self.end_date <= self.start_date:
            raise ValidationError('End date must be after the start date.')

    def __str__(self):
        return str(self.job)



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)






