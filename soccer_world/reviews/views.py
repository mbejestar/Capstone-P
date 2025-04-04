from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action  # Ensure this is imported
from .models import Review  
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):  
    queryset = Review.objects.all()  
    serializer_class = ReviewSerializer 

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])  
    def toggle_lock(self, request, pk=None):  
        review = self.get_object()  
        if review.user != request.user:  
            return Response({'detail': 'You cannot modify this review'}, status=status.HTTP_403_FORBIDDEN)  
        review.locked = not review.locked  # Toggle the locked status
        review.save()  
        return Response({'detail': 'Review lock status updated'}, status=status.HTTP_200_OK)  
    
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)  # Automatically save the user as the current authenticated user  

    def get_queryset(self):  
        # Allow users to see their own reviews as well as all reviews
        # Change this to show all reviews if required
        return Review.objects.filter(user=self.request.user)  # Filter to show only the user's own reviews
