from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Team, Match
from django.db.models import Q, F
import json

TEAMS = [
    {"id": 1, "name": "Реал Мадрид", "country": "Испания"},
    {"id": 2, "name": "Челси", "country": "Англия"}
]

MATCHES = [
    {"id": 1, "home_team": 1, "away_team": 2, "date": "2023-10-15"}
]

@require_http_methods(["GET"])
def profile(request):
    return JsonResponse({
        "username": "test_user",
        "email": "user@example.com",
        "favorite_teams": [1],
        "favorite_matches": []
    })


@require_http_methods(["POST"])
def add_favorite(request):
    try:
        data = json.loads(request.body)
        item_type = data.get('type')
        item_id = data.get('id')
        
        return JsonResponse({
            "status": "success",
            "message": f"{item_type} {item_id} added to favorites"
        }, status=201)
    except:
        return JsonResponse({"error": "Invalid data"}, status=400)
    
@require_http_methods(["GET"])
def search(request):
    query = request.GET.get("q", "").strip().lower()

    teams = Team.objects.filter(
        Q(name__icontains=query) | Q(country__icontains=query)
    ).values("id", "name", "country")

    matches = Match.objects.filter(
        Q(home_team__name__icontains=query) |
        Q(away_team__name__icontains=query)
    ).select_related("home_team", "away_team")

    match_results = [
        {
            "id": m.id,
            "home_team": m.home_team.name,
            "away_team": m.away_team.name,
            "date": m.date
        }
        for m in matches
    ]

    return JsonResponse({
        "teams": list(teams),
        "matches": match_results
    })

@require_http_methods(["GET"])
def team_list(request):
    teams = Team.objects.all().values("id", "name", "country", "foundation_date", "stadium")
    return JsonResponse({"results": list(teams)})

@require_http_methods(["GET"])
def match_list(request):
    matches = Match.objects.select_related("home_team", "away_team").values(
        "id",
        "date",
        "city",
        "home_score",
        "away_score",
        home_team_name=F("home_team__name"),
        away_team_name=F("away_team__name"),
    )
    return JsonResponse({"results": list(matches)})


@require_http_methods(["GET"])
def player_list(request):
    players = Player.objects.select_related("team").values("id", "name", "position", "number", "team__name")
    return JsonResponse({"results": list(players)})

@csrf_exempt
@require_http_methods(["POST"])
def team_create(request):
    try:
        data = json.loads(request.body)
        team = Team.objects.create(
            name=data["name"],
            country=data["country"],
            foundation_date=data["foundation_date"],
            stadium=data.get("stadium", "")
        )
        return JsonResponse({
            "id": team.id,
            "name": team.name,
            "country": team.country,
            "foundation_date": team.foundation_date,
            "stadium": team.stadium
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt    
@require_http_methods(["POST"])
def match_create(request):
    try:
        data = json.loads(request.body)
        home_team = Team.objects.get(id=data["home_team"])
        away_team = Team.objects.get(id=data["away_team"])

        match = Match.objects.create(
            home_team=home_team,
            away_team=away_team,
            city=data["city"],
            date=data["date"]
        )
        return JsonResponse({
            "id": match.id,
            "home_team": home_team.name,
            "away_team": away_team.name,
            "city": match.city,
            "date": match.date
        }, status=201)
    except Team.DoesNotExist:
        return JsonResponse({"error": "Одна из указанных команд не найдена"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def player_create(request):
    try:
        data = json.loads(request.body)
        player = Player.objects.create(
            name=data["name"],
            position=data["position"],
            number=data["number"],
            team_id=data["team_id"],
            birth_date=data["birth_date"]
        )
        return JsonResponse({
            "id": player.id,
            "name": player.name,
            "position": player.get_position_display(),
            "number": player.number,
            "team": player.team.name,
            "birth_date": player.birth_date
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)