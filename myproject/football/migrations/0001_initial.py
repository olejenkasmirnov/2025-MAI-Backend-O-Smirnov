# Generated by Django 5.0.6 on 2025-05-02 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название команды')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('foundation_date', models.DateField(verbose_name='Дата основания')),
                ('stadium', models.CharField(blank=True, max_length=100, verbose_name='Домашний стадион')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя игрока')),
                ('position', models.CharField(choices=[('GK', 'Вратарь'), ('DF', 'Защитник'), ('MF', 'Полузащитник'), ('FW', 'Нападающий')], max_length=2, verbose_name='Позиция')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Игровой номер')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='football.team', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город проведения')),
                ('date', models.DateTimeField(verbose_name='Дата и время матча')),
                ('home_score', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Голы хозяев')),
                ('away_score', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Голы гостей')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='football.team', verbose_name='Гости')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='football.team', verbose_name='Хозяева')),
            ],
            options={
                'verbose_name': 'Матч',
                'verbose_name_plural': 'Матчи',
                'ordering': ['-date'],
            },
        ),
    ]
