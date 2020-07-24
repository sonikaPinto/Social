from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from posts import models
from posts import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class PostListClass(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')

class UserPostClass(generic.ListView):
    model = model.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.get(username__iexact=self.kwargs.get('username')).prefetch_related('user_post')
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post.user.user_post.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post.user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields =('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','post')
    success_url =reverse_lazy('posts:list_post')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = SelectRelatedMixinf.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
