from rest_framework import serializers  
from .models import Review  

class ReviewSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Review  
        fields = ['id', 'team', 'user', 'rating', 'comment']  
        read_only_fields = ['user']  # Prevent user from being set via the API directly  