# users/views.py  
from django.contrib.auth.models import User  
from rest_framework import permissions, generics  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.serializers import AuthTokenSerializer  

class RegisterView(generics.CreateAPIView):  
    queryset = User.objects.all()  
    permission_classes = [permissions.AllowAny]  
    serializer_class = UserSerializer  # You need to create this serializer.  

class CustomAuthToken(ObtainAuthToken):  
    def post(self, request, *args, **kwargs):  
        serializer = self.serializer_class(data=request.data)  
        serializer.is_valid(raise_exception=True)  

        user = serializer.validated_data['user']  
        token, created = Token.objects.get_or_create(user=user)  

        return Response({'token': token.key})  