from rest_framework import views, viewsets, permissions
from rest_framework.response import Response
from django_ratelimit.decorators import ratelimit
from .models import Team
from .serializers import TeamSerializer

class TeamStatisticsView(views.APIView):  
    permission_classes = [permissions.AllowAny] 

    def get(self, request):  
        team_stats = []  
        for team in Team.objects.all():  
            stats = {  
                'name': team.name,  
                'average_rating': team.average_rating(),  
                'number_of_reviews': team.number_of_reviews(),  
            }  
            team_stats.append(stats)  
        return Response(team_stats)  

class TeamViewSet(viewsets.ModelViewSet):  
    queryset = Team.objects.all()  
    serializer_class = TeamSerializer  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)  
    def list(self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)  

    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)  
    def retrieve(self, request, *args, **kwargs):  
        return super().retrieve(request, *args, **kwargs)  

    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)  
    def create(self, request, *args, **kwargs):  
        return super().create(request, *args, **kwargs)  

    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)  
    def update(self, request, *args, **kwargs):  
        return super().update(request, *args, **kwargs)  

    @ratelimit(key='ip', rate='5/m', method='ALL', block=True)  
    def destroy(self, request, *args, **kwargs):  
        return super().destroy(request, *args, **kwargs)  
