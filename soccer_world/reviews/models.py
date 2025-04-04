from django.db import models  
from django.contrib.auth.models import User  
from teams.models import Team  

class Review(models.Model):  
    team = models.ForeignKey(Team, related_name='reviews', on_delete=models.CASCADE)  
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)  
    rating = models.IntegerField()  
    comment = models.TextField()  

    def __str__(self):  
        return f'Review for {self.team.name} by {self.user.username}'  