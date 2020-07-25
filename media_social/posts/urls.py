from django.urls import path,include
from posts import views

app_name = 'posts'
urlpatterns = [
    path('',views.PostListClass.as_view(),name='list_post'),
    path('new/',views.CreatePost.as_view(),name='create_post'),
    path('by/<slug:slug>/',views.UserPostClass.as_view(),name='for_user_post'),
    path('by/<slug:slug>/<int:pk>/',views.PostDetail.as_view(),name='detail_post'),
    path('delete/<int:pk>/',views.DeletePost.as_view(),name='delete_post')
    ]
