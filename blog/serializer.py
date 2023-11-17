from rest_framework import serializers
from blog.models import UserModel
from blog.models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'name',
            'profile',
            'email',
            'password'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = (
            "userid",
            "title",
            "message"
        )