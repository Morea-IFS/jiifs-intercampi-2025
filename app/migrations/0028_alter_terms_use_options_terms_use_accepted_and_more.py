from django.db import migrations, models
 
 
class Migration(migrations.Migration):
 
     dependencies = [
         ('app', '0027_alter_team_photo'),
     ]
 
     operations = [
         migrations.AlterModelOptions(
             name='terms_use',
             options={'ordering': ['-date_accept'], 'verbose_name': 'Terms_Use', 'verbose_name_plural': 'Terms_uses'},
         ),
         migrations.AddField(
             model_name='terms_use',
             name='accepted',
             field=models.BooleanField(default=False),
         ),
         migrations.AddField(
             model_name='terms_use',
             name='document',
             field=models.FileField(blank=True, upload_to='document_boss/'),
         ),
         migrations.AddField(
             model_name='terms_use',
             name='name',
             field=models.CharField(blank=True, max_length=150),
         ),
         migrations.AddField(
             model_name='terms_use',
             name='photo',
             field=models.FileField(blank=True, upload_to='photo_boss/'),
         ),
         migrations.AddField(
             model_name='terms_use',
             name='siape',
             field=models.CharField(blank=True, max_length=150),
         ),
     ]