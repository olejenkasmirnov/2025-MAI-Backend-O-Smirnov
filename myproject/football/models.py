from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название команды")
    country = models.CharField(max_length=50, verbose_name="Страна")
    foundation_date = models.DateField(verbose_name="Дата основания")
    stadium = models.CharField(max_length=100, verbose_name="Домашний стадион", blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class Player(models.Model):
    POSITIONS = [
        ('GK', 'Вратарь'),
        ('DF', 'Защитник'),
        ('MF', 'Полузащитник'),
        ('FW', 'Нападающий'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя игрока")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players", verbose_name="Команда")
    position = models.CharField(max_length=2, choices=POSITIONS, verbose_name="Позиция")
    number = models.PositiveSmallIntegerField(verbose_name="Игровой номер")
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.team})"

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_matches", verbose_name="Хозяева")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_matches", verbose_name="Гости")
    city = models.CharField(max_length=100, verbose_name="Город проведения")
    date = models.DateTimeField(verbose_name="Дата и время матча")
    home_score = models.PositiveSmallIntegerField(verbose_name="Голы хозяев", null=True, blank=True)
    away_score = models.PositiveSmallIntegerField(verbose_name="Голы гостей", null=True, blank=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.date.date()})"

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"
        ordering = ['-date']

"""
from football.models import Team, Player, Match
from django.utils.timezone import now
from datetime import timedelta

# Создание команд
realm = Team.objects.create(name="Реал Мадрид", country="Испания", foundation_date="1902-03-06", stadium="Сантьяго Бернабеу")
chelsea = Team.objects.create(name="Челси", country="Англия", foundation_date="1905-03-10", stadium="Стэмфорд Бридж")
realb = Team.objects.create(name="Реал Бетис", country="Испания", foundation_date="1907-09-12", stadium="Бенито Вильямарин")
reals = Team.objects.create(name="Реал Сосьедад", country="Испания", foundation_date="1909-09-07", stadium="Аноэта")
vreal = Team.objects.create(name="Вильярреал", country="Испания", foundation_date="1923-03-10", stadium="Эстадио де ла Серамика")


# Создание игроков
Player.objects.create(name="Тибо Куртуа", team=realm, position="GK", number=1, birth_date="1992-05-11")
Player.objects.create(name="Винисиус Жуниор", team=realm, position="FW", number=7, birth_date="2000-07-12")
Player.objects.create(name="Коул Палмер", team=chelsea, position="MF", number=20, birth_date="2002-05-06")

# Создание матча
Match.objects.create(
    home_team=realm,
    away_team=chelsea,
    city="Мадрид",
    date=now() + timedelta(days=3),
    home_score=2,
    away_score=1
)


{
  "name": "Антони"
  "position": "FW",
  "number": 7,
  "team_id": 3,
  "birth_date" : "2000-02-24"
}
"""