# Generated by Django 5.1.3 on 2025-04-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_settings_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, default='defaults/team.png', null=True, upload_to='logo_team/'),
        ),
    ]
