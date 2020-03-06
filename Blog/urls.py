"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth_views  # for login n logout view it's default
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('webblog.urls')), # we can keep path empty '' instead of 'webblog0/'   if we do so it will
                              # directly give us a home page without typping webblog0/ at end of url '127..8000'
    path('admin/', admin.site.urls,name='adminpage'),
    path('loginpage/', auth_views.LoginView.as_view(template_name='loginpage.html'), name='loginpage'),
    path('logoutpage/', auth_views.LogoutView.as_view(template_name='logoutpage.html'), name='logoutpage'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                       name='password_reset_complete'),
    path('profile/', user_view.profile, name='profilepage'),
    path('registerpage/', user_view.registration, name='registerpage'),
         # name='loginpage' is to add in html file ,'loginpage/' is for direct url entry


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
