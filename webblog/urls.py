from django.urls import path
from  .views import (PostListview,
                      PostDetailview,
                      PostCreateview,
                      PostUpdateview,
                      PostDeleteview,
                      UserListview,
                      )
from . import views    # . indicates current directory


urlpatterns = [
    path('', PostListview.as_view(), name='webblog-home'),
    path('user/<str:username>', UserListview.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailview.as_view(), name='post_detail'),
    path('post/new/', PostCreateview.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateview.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post_confirmdelete'),
    path('about/', views.about, name='webblog-about'),



]
