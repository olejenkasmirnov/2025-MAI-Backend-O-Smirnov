from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
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

@require_http_methods(["GET"])
def team_list(request):
    return JsonResponse({
        "count": len(TEAMS),
        "results": TEAMS
    })

@require_http_methods(["GET"])
def team_detail(request, team_id):
    team = next((t for t in TEAMS if t["id"] == team_id), None)
    if team:
        return JsonResponse(team)
    return JsonResponse({"error": "Not found"}, status=404)

@require_http_methods(["GET"])
def match_list(request):
    page = int(request.GET.get('page', 1))
    per_page = 2
    start = (page-1)*per_page
    end = start + per_page
    
    return JsonResponse({
        "page": page,
        "results": MATCHES[start:end],
        "total": len(MATCHES)
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