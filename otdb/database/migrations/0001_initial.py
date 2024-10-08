# Generated by Django 5.0.6 on 2024-09-12 02:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from database.models import UserRolesField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeatmapMetadata',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('difficulty', models.CharField(max_length=256)),
                ('ar', models.FloatField()),
                ('od', models.FloatField()),
                ('cs', models.FloatField()),
                ('hp', models.FloatField()),
                ('length', models.PositiveIntegerField()),
                ('bpm', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BeatmapMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=2)),
                ('settings', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeatmapsetMetadata',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('creator', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Mappool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('avg_star_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MappoolBeatmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MappoolBeatmapConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='MappoolConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_override', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MappoolFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('abbreviation', models.CharField(default='', max_length=16)),
                ('link', models.CharField(default='', max_length=256)),
                ('description', models.CharField(default='', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TournamentInvolvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', UserRolesField(default=0)),
            ],
        ),
        migrations.AddConstraint(
            model_name='beatmapmod',
            constraint=models.UniqueConstraint(fields=('acronym', 'settings'), name='beatmapmod_unique_constraint'),
        ),
        migrations.AddField(
            model_name='mappool',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitted_mappools', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mappoolbeatmap',
            name='beatmap_metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mappool_beatmaps', to='database.beatmapmetadata'),
        ),
        migrations.AddField(
            model_name='mappoolbeatmap',
            name='beatmapset_metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mappool_beatmaps', to='database.beatmapsetmetadata'),
        ),
        migrations.AddField(
            model_name='mappoolbeatmap',
            name='mods',
            field=models.ManyToManyField(related_name='related_beatmaps', to='database.beatmapmod'),
        ),
        migrations.AddField(
            model_name='mappoolbeatmapconnection',
            name='beatmaps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappool_connections', to='database.mappoolbeatmap'),
        ),
        migrations.AddField(
            model_name='mappoolbeatmapconnection',
            name='mappool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beatmap_connections', to='database.mappool'),
        ),
        migrations.AddField(
            model_name='mappool',
            name='beatmaps',
            field=models.ManyToManyField(related_name='mappools', through='database.MappoolBeatmapConnection', to='database.mappoolbeatmap'),
        ),
        migrations.AddField(
            model_name='mappoolconnection',
            name='mappool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament_connections', to='database.mappool'),
        ),
        migrations.AddField(
            model_name='mappoolfavorite',
            name='mappool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.mappool'),
        ),
        migrations.AddField(
            model_name='mappoolfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mappool',
            name='favorites',
            field=models.ManyToManyField(related_name='mappool_favorites', through='database.MappoolFavorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournament',
            name='mappools',
            field=models.ManyToManyField(through='database.MappoolConnection', to='database.mappool'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='submitted_tournaments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mappoolconnection',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappool_connections', to='database.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentfavorite',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournament',
            name='favorites',
            field=models.ManyToManyField(related_name='tournament_favorites', through='database.TournamentFavorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournamentinvolvement',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='involvements', to='database.tournament'),
        ),
        migrations.AddField(
            model_name='tournamentinvolvement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournament',
            name='involved_users',
            field=models.ManyToManyField(through='database.TournamentInvolvement', to=settings.AUTH_USER_MODEL),
        ),
    ]
