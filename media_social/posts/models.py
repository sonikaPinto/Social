from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_post')
    created_time = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False,default='',blank=True)
    group = models.ForeignKey(Group,related_name='group_post',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-created_time']
        unique_together = ['user','message']
