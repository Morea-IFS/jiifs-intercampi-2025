# Generated by Django 5.1.3 on 2025-03-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_player_team_sport_team_sport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='file',
            field=models.FileField(blank=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='voluntary',
            name='type_voluntary',
            field=models.IntegerField(choices=[(0, 'Voluntario'), (2, 'Organização'), (1, 'Técnico'), (3, 'Chefe de delegação')], default=0),
        ),
    ]
