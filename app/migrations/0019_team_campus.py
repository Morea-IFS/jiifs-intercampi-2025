# Generated by Django 5.1.3 on 2025-02-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_player_bulletin'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='campus',
            field=models.IntegerField(choices=[(0, 'Lagarto'), (1, 'Aracaju'), (2, 'Socorro'), (3, 'Poço Redondo'), (4, 'São Cristovão'), (5, 'Itabaiana'), (6, 'Glória'), (7, 'Estância'), (8, 'Propriá'), (9, 'Tobias Barreto'), (10, 'Reitoria')], default=10),
        ),
    ]
