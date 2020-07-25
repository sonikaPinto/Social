from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class CreateGroup(generic.CreateView,LoginRequiredMixin):
    fields = ('name','description')
    model = Group
    success_url=reverse_lazy('groups:group_list')

class ListGroups(generic.ListView):
    model = Group

class GroupDetails(generic.DetailView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except:
            messages.warning(self.request,'Warning! Already a member')
        else:
            messages.success(self.request,'you are now a member')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except:
            messages.warning(self.request,'You arent in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You are removed from the group')
        return super().get(request,*args,**kwargs)
