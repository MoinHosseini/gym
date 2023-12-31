# Generated by Django 4.2.1 on 2023-09-19 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fitness_goal', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('bmi', models.FloatField()),
                ('workout_schedule', models.JSONField(default={})),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trainer')),
            ],
        ),
    ]
