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