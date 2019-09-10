from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for our API View"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')  #pass a tuple
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }    

    def create(self, validated_data):
        """Create and return a new user,it overrides the default create function."""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user   
        