from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime
from django.utils import timezone

# Create your models here.

class Status(models.IntegerChoices):
    shortly = 0, "Em breve"
    happening = 1, "Acontecendo"
    finished = 2, "Finalizada"
    cancelado = 3, "Cancelada"
    paused = 4, "Pausada"
    empty = 5, "Nenhum"

class Sport_types(models.IntegerChoices):
    futsal = 0, "Futsal"
    volleyball = 1, "Voleibol"
    volley_sitting = 2, "Voleibol sentado"
    handball = 3, "Handebol"
    chess = 4, "Xadrez"
    table_tennis = 5, "Tênis de mesa"
    race = 6, "100 M"
    high_jump = 7, "Salto em distância"
    launch_dart = 8, "Lançamento de dardo"
    pitch_weight = 9, "Lançamento de peso"

class Campus_types(models.IntegerChoices):
    aracaju = 0, "Aracaju"
    estancia = 1, "Estância"
    gloria = 2, "Glória"
    itabaiana = 3, "Itabaiana"
    lagarto = 4, "Lagarto"
    poco_redondo = 5, "Poço Redondo"
    propria = 6, "Propriá"
    sao_cristovao = 7, "São Cristovão"
    socorro = 8, "Socorro"
    tobias_barreto = 9, "Tobias Barreto"
    reitoria = 10, "Reitoria"

class Point_types(models.IntegerChoices):
    goal = 0, "Gol"
    point = 1, "Ponto"
    ace = 2, "Ace"
    empty = 3, "Nenhum"

class Activity(models.IntegerChoices):
    holder = 0, "Titular"
    reserve = 1, "Reserva"
    empty = 2, "Nenhum"

class Type_penalties(models.IntegerChoices):
    card_red = 0, "Cartão Vermelho"
    card_yellow = 1, "Cartão Amarelo"
    lack = 2, "lack"
    empty = 3, "Nenhum"

class Sexo_types(models.IntegerChoices):
    masculine = 0, "Masculino"
    feminine = 1, "Feminino"
    mixed = 2, "Misto"

class Type_Banner(models.IntegerChoices):
    In_use = 0, "Em uso"
    empty = 1, "Nenhum"

class Type_service(models.IntegerChoices):
    voluntary = 0, "Voluntario"
    organization = 2, "Organização"
    technician = 1, "Técnico"
    head_delegation = 3,"Chefe de delegação"

class Settings_access(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):    
        return f"{self.start} | {self.end}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photo_player/', default='defaults/person.png', blank=True)
    bulletin = models.FileField(upload_to='bulletins/')
    sexo = models.IntegerField(choices=Sexo_types.choices, default=Sexo_types.mixed)
    campus = models.IntegerField(choices=Campus_types.choices, default=Campus_types.reitoria)
    registration = models.CharField(max_length=15, default="0000000000")
    cpf = models.CharField(max_length=11, default="00000000000")
    date_nasc = models.DateField(default=timezone.now)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):    
        return f"{self.name} | {self.sexo} | {self.admin.username}"
    
class Technician(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    siape = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photo_technician/', default='defaults/person.png', blank=True)
    campus = models.IntegerField(choices=Campus_types.choices, default=Campus_types.reitoria)
    sexo = models.IntegerField(choices=Sexo_types.choices, default=Sexo_types.mixed)

    def __str__(self):    
        return f"{self.name} | {self.sexo}"
    
class Voluntary(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo_voluntary/', default='defaults/person.png', blank=True)
    campus = models.IntegerField(choices=Campus_types.choices, default=Campus_types.reitoria)
    registration = models.CharField(max_length=11, default="00000000000")
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type_voluntary = models.IntegerField(choices=Type_service.choices, default=Type_service.voluntary)

    def __str__(self):    
        return f"{self.name} | {self.get_campus_display()}"

class Team(models.Model):
    name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='logo_team/', default='defaults/team.png', blank=True)
    hexcolor = models.CharField(max_length=7, null=True, blank=True)
    campus = models.IntegerField(choices=Campus_types.choices, default=Campus_types.reitoria)

    def __str__(self):    
        return f"{self.name}"


class Badge(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='badge/', blank=True)

    def __str__(self):    
        return f"{self.name} - {self.id}"
    
class Attachments(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/', blank=True)

    def __str__(self):    
        return f"{self.name} - {self.id}"

class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='certificate/', blank=True)

    def __str__(self):    
        return f"{self.name}"

class Team_sport(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sport = models.IntegerField(choices=Sport_types.choices)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    sexo = models.IntegerField(choices=Sexo_types.choices)
    status = models.BooleanField(default=False)

    def __str__(self):    
        return f"{self.team} | {self.get_sport_display()}"
    
class Player_team_sport(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_sport = models.ForeignKey(Team_sport, on_delete=models.CASCADE, related_name="players")

    def __str__(self):    
        return f"{self.player} | {self.team_sport}"

class Team_match(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey('Match', on_delete=models.CASCADE, related_name='teams')

    def __str__(self):    
        return f"{self.team} | {self.match}"

class Volley_match(models.Model):
    status = models.IntegerField(choices=Status.choices, default=Status.empty)
    sets_team_a = models.IntegerField(default=0)
    sets_team_b = models.IntegerField(default=0)

    def __str__(self):    
        return f"{self.get_status_display()} | {self.sets_team_a} | {self.sets_team_b}"

class Match(models.Model):
    sport = models.IntegerField(choices=Sport_types.choices)
    status = models.IntegerField(choices=Status.choices, default=Status.shortly)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    sexo = models.IntegerField(choices=Sexo_types.choices, default=Sexo_types.mixed, blank=True)
    mvp_player_player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    Winner_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    volley_match = models.ForeignKey(Volley_match, on_delete=models.CASCADE, blank=True, null=True, related_name="matches")
    add = models.TimeField(blank=True, null=True)
    time_match = models.DateTimeField(null=True, blank=True)

    def __str__(self):    
        return f"{self.id} | {self.get_sport_display()} | {self.get_status_display()} | {self.sexo}"

class Point(models.Model):
    point_types = models.IntegerField(choices=Point_types.choices, default=Point_types.empty)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    team_match = models.ForeignKey(Team_match, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):    
        if self.player:
            return f"{self.point_types} | {self.player} | {self.team_match} | {self.time}"
        else:
            return f"{self.point_types} | {self.team_match} | {self.time}"

class Assistance(models.Model):
    assis_to = models.ForeignKey(Point, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)

    def __str__(self):    
        return f"{self.assis_to} | {self.player}"

class Player_match(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_number = models.IntegerField(blank=True, null=True, default=0)
    activity = models.IntegerField(choices=Activity.choices, default=Activity.empty)
    team_match = models.ForeignKey(Team_match, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):    
        return f"{self.player} | {self.match} | {self.player_number} | {self.team_match} | {self.get_activity_display()}" 
class Penalties(models.Model):
    type_penalties = models.IntegerField(choices=Type_penalties.choices, default=Type_penalties.empty)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    team_match = models.ForeignKey(Team_match, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):    
        return f"{self.get_type_penalties_display()} | {self.player} | {self.team_match} | {self.time}"

class Time_pause(models.Model):
    start_pause = models.TimeField()
    end_pause = models.TimeField(null=True, blank=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):    
        if self.start_pause:
            return f"{self.start_pause} | {self.match}"
        elif self.start_pause and self.end_pause:
            return f"{self.start_pause} | {self.end_pause} | {self.match}"

class Events(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    datetime = models.TimeField(auto_now_add=True)

    def __str__(self):    
        return f"{self.name} | {self.details} | {self.details} | {self.datetime}"
    
class Config(models.Model):
    site = models.CharField(max_length=200,null=True, blank=True)
    qrcode = models.ImageField(upload_to='photos_config/', default='defaults/qrcode.png',null=True, blank=True)
    areasup = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):    
        return f"{self.id} | {self.site}"
    
class Banner(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='photos_config/', null=True, blank=True)
    status = models.IntegerField(choices=Type_Banner.choices, default=Type_Banner.empty)

    def __str__(self):    
        return f"{self.id} | {self.name} | {self.status}"

class Terms_Use(models.Model):
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date_accept = models.DateTimeField(auto_now_add=True)

    @property
    def date_accept_local(self):
        return localtime(self.date_accept)

    def __str__(self):
        return f"{self.usuario} - {self.date_accept_local.strftime('%d/%m/%Y %H:%M:%S')}"
    
class Bolletin(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class Section(models.Model):
    bolletin = models.ForeignKey(Bolletin, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=500)
    contend = models.CharField(max_length=1500)
