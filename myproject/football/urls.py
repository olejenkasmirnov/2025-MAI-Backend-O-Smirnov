from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('teams/', views.team_list),
    path('teams/<int:team_id>/', views.team_detail),
    path('matches/', views.match_list),
    path('favorites/', views.add_favorite),
]