from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import TeamViewSet  
from .views import TeamStatisticsView  

router = DefaultRouter()  
router.register(r'teams', TeamViewSet)  

urlpatterns = [  
    path('statistics/', TeamStatisticsView.as_view(), name='team-statistics'),  
    path('', include(router.urls)),  
]  
