from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount
from . import models

# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Post)
# admin.site.register(LikePost)
admin.site.register(FollowersCount)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): 
    list_display = ('id_user','bio','location')

admin.site.register(Post)
admin.site.register(LikePost)