from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
#from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView    # for Class based Views
from .models import *

# by views we can render webpage by two way 1. function based view 2. class based view
# first we used function based view but class based view offered very good functionality we later use that


# def home(request):      # this is function based view
#         context={
#             'posts': Post.objects.all()
#         }
#
#         return render(request, 'home.html', context)   #html files are stored in templates folder in Blog folder

def about(request):
    return render(request, 'about.html', )



# Class based View Below!!

class PostListview(ListView):
    # here model, template_name, context_object_name  are default keyword of class ListView
    model = Post  # Post is our model class we had defined in model.py n that we need to use this here
    template_name = 'home.html'  # <appname>/<model>_<Listview>.html      ## add in this format django looks file in this format
    context_object_name = 'posts'  # name that use in out html page to to refer class Post in model.py
    ordering = ['-date_posted']   # we want to order our database(ultimately post in page), '-' here indidcates we want post newest to oldest
    paginate_by = 5      ## Keyword of Listview for Pagination so it will limit 5 post per page


class UserListview(ListView): # similar to above listview but it will show all post of specific user when we click on its name
    model = Post
    template_name = 'specificUser_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):    # it's default method
        user=get_object_or_404(User, username=self.kwargs.get('username'))   # to get username
        return Post.objects.filter(author=user).order_by('-date_posted')




class PostDetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateview(LoginRequiredMixin, CreateView):   # LoginRequiredMixin is like LoginRequired decorated as in functional base view
                                                            # it will not allow to create new post without login
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    def form_valid(self, form):        #  to link new created post with its author(logged in user)
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateview(UserPassesTestMixin, LoginRequiredMixin, UpdateView):  # UserPassesTestMixin will only allow to update post created by author itself
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):  # to link new created post with its author(logged in user)
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):       ## this default fun will test user whether user is trying to update post of someone else or its own
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteview(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_ConfirmDelete.html'
    success_url = '/'   # after delete post page will be redirect to this url which is home

    def test_func(self):  ## this default fun will test user whether user is trying to update post of someone else or its own
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
