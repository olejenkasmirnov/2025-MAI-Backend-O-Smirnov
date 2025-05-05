from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('teams/', views.team_list),
    path('matches/', views.match_list),
    path('players/', views.player_list),
    path('teams/create/', views.team_create),
    path('matches/create/', views.match_create),
    path('players/create/', views.player_create),
    path('favorites/', views.add_favorite),
    path('search/', views.search)
]
