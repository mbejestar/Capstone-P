from django.db import models  

class Team(models.Model):  
    name = models.CharField(max_length=100)  
    city = models.CharField(max_length=100)  
    league = models.CharField(max_length=100)  
    description = models.TextField()  
    founded_year = models.IntegerField()
    logo = models.ImageField(upload_to='team_logos/')

    def __str__(self):  
        return self.name  
