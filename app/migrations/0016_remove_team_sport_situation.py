# Generated by Django 5.1.3 on 2025-02-14 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_technician_campus_alter_match_sport_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_sport',
            name='situation',
        ),
    ]
