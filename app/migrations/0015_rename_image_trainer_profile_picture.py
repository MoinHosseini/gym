# Generated by Django 4.2.1 on 2023-09-19 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_trainer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='image',
            new_name='profile_picture',
        ),
    ]