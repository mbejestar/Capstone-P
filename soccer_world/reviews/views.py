from rest_framework import viewsets, permissions  
from .models import Review  
from .serializers import ReviewSerializer  

class ReviewViewSet(viewsets.ModelViewSet):  
    queryset = Review.objects.all()  
    serializer_class = ReviewSerializer  
    
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)  # Save the user as the current authenticated user  

    def get_queryset(self):  
        # Allow users to see their own reviews as well as all reviews  
        return Review.objects.filter(user=self.request.user)  