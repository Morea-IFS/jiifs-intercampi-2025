from django.contrib import admin
from . models import Certificate, Badge, Config, Volley_match, Events, Player, Voluntary, Technician, Assistance, Penalties, Time_pause, Team, Point, Team_sport, Player_team_sport, Match, Team_match, Player_match, Banner, Terms_Use

# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','name','sexo','campus','registration','date_nasc','bulletin','photo')
    search_fields = ('id','name','sexo','campus','registration','date_nasc','bulletin','photo')

@admin.register(Badge)
class BadgevAdmin(admin.ModelAdmin):
    list_display = ('id','name','user','file')
    search_fields = ('id','name','user','file')

@admin.register(Certificate)
class CertificatevAdmin(admin.ModelAdmin):
    list_display = ('id','name','user','file')
    search_fields = ('id','name','user','file')

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('id','name','sexo', 'siape','campus')
    search_fields = ('id','name','sexo', 'siape','campus')

@admin.register(Voluntary)
class VoluntaryAdmin(admin.ModelAdmin):
    list_display = ('id','name','registration','campus')
    search_fields = ('id','name','registration','campus')

@admin.register(Volley_match)
class Volley_matchAdmin(admin.ModelAdmin):
    list_display = ('id','status','sets_team_a','sets_team_b')
    search_fields = ('id','status','sets_team_a','sets_team_b')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name','hexcolor')
    search_fields = ('id','name','hexcolor')

@admin.register(Team_sport)
class Team_sportAdmin(admin.ModelAdmin):
    list_display = ('id','team','sport','sexo','admin')
    search_fields = ('id','team','sport','sexo','admin')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id','sexo','sport','time_match','status','Winner_team','time_start','time_end')
    search_fields = ('id','sexo','sport','time_match','status','Winner_team','time_start','time_end')

@admin.register(Player_match)
class Player_matchAdmin(admin.ModelAdmin):
    list_display = ('id','match','player_number','player')
    search_fields = ('id','match','player_number','player')

@admin.register(Team_match)
class Team_matchAdmin(admin.ModelAdmin):
    list_display = ('id','team','match')
    search_fields = ('id','team','match')

@admin.register(Player_team_sport)
class Team_sportAdmin(admin.ModelAdmin):
    list_display = ('id','player','team_sport')
    search_fields = ('id','player','team_sport')

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('id','point_types','player','team_match','time')
    search_fields = ('id','point_types','player','team_match','time')

@admin.register(Penalties)
class PenaltiesAdmin(admin.ModelAdmin):
    list_display = ('id','type_penalties','player','team_match','time')
    search_fields = ('id','type_penalties','player','team_match','time')

@admin.register(Time_pause)
class Time_pauseAdmin(admin.ModelAdmin):
    list_display = ('id','start_pause','end_pause','match')
    search_fields = ('id','start_pause','end_pause','match')

@admin.register(Assistance)
class AssistanceAdmin(admin.ModelAdmin):
    list_display = ('id','assis_to','player','match')
    search_fields = ('id','assis_to','player','match')

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id','name','details')
    search_fields = ('id','name','details')

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id','site')
    search_fields = ('id','site')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','name','status')
    search_fields = ('id','name','status')

@admin.register(Terms_Use)
class Terms_UseAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'date_accept_local')