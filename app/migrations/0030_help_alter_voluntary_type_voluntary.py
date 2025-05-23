# Generated by Django 5.1.3 on 2025-04-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_terms_use_options_remove_terms_use_accepted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='voluntary',
            name='type_voluntary',
            field=models.IntegerField(choices=[(0, 'Voluntario'), (1, 'Técnico de modalidade esportiva'), (2, 'Apoio'), (3, 'Estagiario'), (4, 'Chefe de delegação')], default=0),
        ),
    ]
