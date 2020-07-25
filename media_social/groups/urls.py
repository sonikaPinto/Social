from django.urls import path,include
from groups import views

app_name = 'groups'
urlpatterns = [
    path('',views.ListGroups.as_view(),name='group_list'),
    path('new/',views.CreateGroup.as_view(),name="create_group"),
    path('<slug:slug>/',views.GroupDetails.as_view(),name='group_detail'),
    path('Leave/<slug:slug>',views.LeaveGroup.as_view(),name='leave'),
    path('Join/<slug:slug>',views.JoinGroup.as_view(),name='join'),
    ]
