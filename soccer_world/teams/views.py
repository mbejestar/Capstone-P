 from rest_framework import views  
from rest_framework.response import Response  
from .models import Team  

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
