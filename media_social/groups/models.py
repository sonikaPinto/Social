from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template
# Create your models here.


User = get_user_model()
#what is this?
from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(unique=True,allow_unicode=True,default='',blank=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,blank=True,default='')
    #what is this
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering =['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='membership')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=('group','user')
