from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.sql.datastructures import Join
from django.db.models.signals import post_save
import datetime as dt

# Create your models here.


class Blog(models.Model):

    '''
    Models that keeps track of the blogs data
    '''

    title = models.CharField(max_length = 50, null = True)
    user = models.ForeignKey(User, related_name = "user_blog", on_delete = models.CASCADE, null = True)
    content = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to='image/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content

    def save_blog(self):
        self.save()

    @classmethod
    def delete_blog_by_id(cls, id):
        blogs = cls.objects.filter(pk=id)
        blogs.delete()

    @classmethod
    def get_blog_by_id(cls, id):
        blogs = cls.objects.get(pk=id)
        return blogs


    @classmethod
    def search_blog(cls, search_term):
        blogs = cls.objects.filter(title__icontains=search_term)
        return blogs

    @classmethod
    def update_blog(cls, id):
        blogs = cls.objects.filter(id=id).update(id=id)
        return blogs


    def get_absolute_url(self):
        return reverse("home", kwargs={"id": self.id})





class Profile(models.Model):

    '''
	Model that keeps track of profile datas
	'''

    bio = models.TextField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email= models.TextField(max_length=200, null=True, blank=True)
    blog_id = models.ForeignKey(Blog, null=True)
  
    

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    def __str__(self):
        return self.user.username  
    

    

