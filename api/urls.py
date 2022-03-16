from django.urls import path
from .views import getLeaderboardByGame, getRankForUser, main, AddorUpdateRankForUser

urlpatterns = [
    path('', main),
    path('leaderboard/<str:game>/', getLeaderboardByGame),
    path('rank/', AddorUpdateRankForUser),
    path('rank/<str:rankHolder>/', getRankForUser),
]
