from rest_framework import serializers
from blog.models import UserModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'name',
            'profile',
            'email',
            'password'
        )