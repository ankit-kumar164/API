from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField, IntegerField
from collections import OrderedDict
from .models import Post , LikePost
from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException



class ContactSerializer(serializers.ModelSerializer):
	   
    id_user = IntegerField(required=True)
    bio = CharField(required=True)
    location = CharField(max_length=100, required=True)
	
    class Meta:
        model = models.Profile
        fields = ('id_user','bio','location')

class NotEnoughStockException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'There is none'
    default_code = 'invalid'




class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','user')




class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikePost
        fields = (
            'post_id',
            'username',
        )
    
    def likes(self,post_id,username):
        likes = LikePost.objects.filter(post_id=id, username=username).first()
        return likes

    def validate(self, res: OrderedDict):
        '''
        Used to validate Item stock levels
        '''
        likes = res.get("likes")
        if not likes:
            raise NotEnoughStockException
        return res