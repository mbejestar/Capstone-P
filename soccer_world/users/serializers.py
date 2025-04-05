from django.contrib.auth.models import User  
from rest_framework import serializers  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'password']  
        extra_kwargs = {  
            'password': {'write_only': True}  # is the password is write-only ? 
        }  

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  # Hash the password  
        user.save()  
        return user  
