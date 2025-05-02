from django.contrib import admin
from .models import Team, Player, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'foundation_date')
    search_fields = ('name', 'country')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'position', 'number')
    list_filter = ('team', 'position')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'date', 'city', 'score_display')
    
    def score_display(self, obj):
        return f"{obj.home_score or '-'}:{obj.away_score or '-'}"
    score_display.short_description = "Счёт"
