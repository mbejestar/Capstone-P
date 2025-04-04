from django.db import models  
from django.db.models import Avg, Count  
from reviews.models import Review  

class Team(models.Model):  
    name = models.CharField(max_length=100)  
    city = models.CharField(max_length=100)  
    league = models.CharField(max_length=100)  
    description = models.TextField()  

    def average_rating(self):  
        """Returns the average rating of this team."""  
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0  

    def number_of_reviews(self):  
        """Returns the number of reviews for this team."""  
        return self.reviews.count()  

    # this is for thhe most popular teams:  
    @staticmethod  
    def get_most_popular_teams(limit=5):  
        return Team.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:limit]  

    def __str__(self):  
        return self.name  
