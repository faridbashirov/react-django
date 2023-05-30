from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
from django.core.mail import send_mail
from django.conf import settings
import random
class AbstractModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Device(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name  


class RepairChoices(models.Model):
    name=models.CharField(max_length=200)
    device=models.ManyToManyField("Device")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="RepairChoice"
        verbose_name_plural="RepairChoices"
    

class Estimate(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    device_type=models.CharField(max_length=100)
    repair_type=models.CharField(max_length=100)
    message=models.TextField()
  

class Client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    device_type=models.CharField(max_length=100,choices=[((f'{i}'),(f'{i}')) for i in Device.objects.all()])
    repair_type=models.CharField(max_length=100,choices=[((f'{i}'),(f'{i}')) for i in RepairChoices.objects.all()])
    status=models.CharField(max_length=100,choices=[("On process","On process"),("Done","Done")])
    email=models.EmailField(null=True,blank=True)
    ticket=models.CharField(max_length=100)
    
    def save(self,*args,**kwargs):
        not_unique = True
        while not_unique:
            unique_ref =random.randint(100000, 999999)
            if  not Client.objects.filter(ticket=unique_ref):
                not_unique = False
        a=str(unique_ref)
        unique_ref=""
        for i in range(len(a)):
             unique_ref+=a[i]
             if i ==2 :
              unique_ref+="-"
        
        self.ticket=unique_ref
        if self.email:
         text = f'Your ticket id for check your device status: {unique_ref} '
         send_mail(
            ' Phone Repair',
            text,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
         )
        return super(Client,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.first_name


class Service(AbstractModel):
    name=models.CharField(max_length=200)
    small_description=models.CharField(max_length=200)
    description=RichTextUploadingField()
    icon=models.ImageField(upload_to='services/', blank=True, null=True)
    image=models.ImageField(upload_to='services/')
    slug=models.SlugField(max_length=250,null=True,blank=True)
    meta_title=models.CharField(max_length=200)
    meta_description=models.CharField(max_length=200)
    meta_keywords=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        return super(Service,self).save(*args,**kwargs)
    
    class Meta:
        ordering=['id'  ]


class BlogCategory(AbstractModel):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250,null=True,blank=True)
    meta_title=models.CharField(max_length=200)
    meta_description=models.CharField(max_length=200)
    meta_keywords=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super(BlogCategory,self).save(*args,**kwargs)
    class Meta:
        verbose_name="BlogCategory"
        verbose_name_plural="BlogCategories"
    

class Blogs(AbstractModel):
    title=models.CharField(max_length=200)
    small_description=models.CharField(max_length=200)
    description=RichTextUploadingField()
    small_description=models.TextField()
    image=models.ImageField(upload_to='services/')
    slug=models.SlugField(max_length=250,null=True,blank=True)
    category=models.ForeignKey("BlogCategory",on_delete=models.CASCADE)
    meta_title=models.CharField(max_length=200)
    meta_description=models.CharField(max_length=200)
    meta_keywords=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super(Blogs,self).save(*args,**kwargs)
    class Meta:
        verbose_name="Blog"
        verbose_name_plural="Blogs"

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contacts"


