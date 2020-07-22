

# Register your models here.
from django.contrib import admin
from app_Blog.models import Blog, Comment, Likes

# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)