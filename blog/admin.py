from django.contrib import admin
from .models import Post

admin.site.register(Post) #makes the model visible on the admin page
