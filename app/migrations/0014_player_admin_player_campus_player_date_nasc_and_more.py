# Generated by Django 5.1.3 on 2025-02-11 18:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_terms_use'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='player',
            name='campus',
            field=models.CharField(default='Reitoria', max_length=50),
        ),
        migrations.AddField(
            model_name='player',
            name='date_nasc',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='player',
            name='registration',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='team_sport',
            name='admin',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_sport',
            name='sexo',
            field=models.IntegerField(choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Misto')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_sport',
            name='situation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='sexo',
            field=models.IntegerField(blank=True, choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Misto')], default=2),
        ),
        migrations.AlterField(
            model_name='match',
            name='sport',
            field=models.IntegerField(choices=[(0, 'Futsal'), (1, 'Voleibol'), (2, 'Voleibol sentado'), (3, 'Handebol'), (4, 'Xadrez'), (5, 'Tênis de mesa'), (6, 'Corrida 100 M'), (7, 'Salto em altura'), (8, 'Queimado')]),
        ),
        migrations.AlterField(
            model_name='player',
            name='sexo',
            field=models.IntegerField(choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Misto')], default=2),
        ),
        migrations.AlterField(
            model_name='team',
            name='hexcolor',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='team_sport',
            name='sport',
            field=models.IntegerField(choices=[(0, 'Futsal'), (1, 'Voleibol'), (2, 'Voleibol sentado'), (3, 'Handebol'), (4, 'Xadrez'), (5, 'Tênis de mesa'), (6, 'Corrida 100 M'), (7, 'Salto em altura'), (8, 'Queimado')]),
        ),
        migrations.AlterField(
            model_name='technician',
            name='sexo',
            field=models.IntegerField(choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Misto')], default=2),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.ImageField(blank=True, upload_to='badge/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('file', models.ImageField(blank=True, upload_to='certificate/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
