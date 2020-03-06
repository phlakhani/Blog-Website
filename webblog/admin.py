from django.contrib import admin
from .models import Post

# Register your models here.
#Registering class models from models.py in admin.py  will make created database modifiable from admin page after login

admin.site.register(Post)