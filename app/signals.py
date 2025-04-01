# app/signals.py
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.templatetags.static import static
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .generators import generate_timer

from .models import Point, Match, Team_match, Team, Penalties, Volley_match, Player_match, Time_pause, Banner, Player_team_sport

default_photo_url = f"{settings.MEDIA_URL}defaults/team.png"

def generate_score_data():
    if Volley_match.objects.filter(status=1):
        volley_match = Volley_match.objects.get(status=1)
        if Match.objects.filter(volley_match=volley_match, status=1):
            volley_match = Volley_match.objects.get(status=1)
            if len(Match.objects.filter(volley_match=volley_match)) > 1:
                match = Match.objects.filter(volley_match=volley_match, status=1).last()
            else:
                match = Match.objects.get(volley_match=volley_match, status=1)
            team_matchs = Team_match.objects.filter(match=match)
            if team_matchs[0]:
                team_match_a = team_matchs[0]
            else:
                match.status = 3
                match.save()
            if team_matchs[1]:
                team_match_b = team_matchs[1]
            else:
                match.status = 3
                match.save()
            if (match.volley_match.sets_team_a + match.volley_match.sets_team_b) % 2 == 0:
                print("par")
                sets_1 = match.volley_match.sets_team_a
                sets_2 = match.volley_match.sets_team_b
                team_1 = team_match_a
                team_2 = team_match_b
                point_1 = Point.objects.filter(team_match=team_match_a).count()
                point_2 = Point.objects.filter(team_match=team_match_b).count()
                aces_1 = Point.objects.filter(point_types=2, team_match=team_match_a).count()
                aces_2 = Point.objects.filter(point_types=2, team_match=team_match_b).count()
                lack_1 = Penalties.objects.filter(type_penalties=2, team_match=team_match_a).count()
                lack_2 = Penalties.objects.filter(type_penalties=2, team_match=team_match_b).count()
                card_1 = Penalties.objects.filter(type_penalties=0,team_match=team_match_a).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_a).count()
                card_2 = Penalties.objects.filter(type_penalties=0,team_match=team_match_b).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_b).count()
            else:
                print("impar")
                sets_1 = match.volley_match.sets_team_b
                sets_2 = match.volley_match.sets_team_a
                team_1 = team_match_b
                team_2 = team_match_a
                point_1 = Point.objects.filter(team_match=team_match_b).count()
                point_2 = Point.objects.filter(team_match=team_match_a).count()
                aces_1 = Point.objects.filter(point_types=2, team_match=team_match_b).count()
                aces_2 = Point.objects.filter(point_types=2, team_match=team_match_a).count()
                lack_1 = Penalties.objects.filter(type_penalties=2, team_match=team_match_b).count()
                lack_2 = Penalties.objects.filter(type_penalties=2, team_match=team_match_a).count()
                card_1 = Penalties.objects.filter(type_penalties=0,team_match=team_match_a).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_a).count()
                card_2 = Penalties.objects.filter(type_penalties=0,team_match=team_match_b).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_b).count()
            point_a = Point.objects.filter(point_types=1, team_match=team_match_a).count()
            point_b = Point.objects.filter(point_types=1, team_match=team_match_b).count()
            aces_a = Point.objects.filter(point_types=2, team_match=team_match_a).count()
            aces_b = Point.objects.filter(point_types=2, team_match=team_match_b).count()
            if Banner.objects.filter(status=0): 
                banner_score = Banner.objects.get(status=0).image.url
                banner_status_score = True
            else: 
                banner_score = static('images/logo-jifs-intercampi.svg')
                banner_status_score = False
            name_scoreboard = 'Sets'
            ball_sport = static('images/ball-of-volley.png')
            if match.sexo == 1: 
                img_sexo = static('images/icon-female.svg')
                sexo_color = '#ff32aa' 
            else: 
                img_sexo = static('images/icon-male.svg')
                sexo_color = '#3a7bd5'
            match_data = {
                'agua': "agua",
                'team_a': team_1.team.name,
                'team_b': team_2.team.name,
                'team_a_score': team_match_a.team.name,
                'team_b_score': team_match_b.team.name,
                'sets_a':sets_1,
                'sets_b':sets_2,
                'teamAcolor': team_1.team.hexcolor,
                'teamBcolor': team_2.team.hexcolor,
                'points_a_score':point_a,
                'points_b_score':point_b,
                'banner_score':banner_score,
                'banner_status_score':banner_status_score,
                'points_a':point_1,
                'points_b':point_2,
                'points_a_score':point_a,
                'points_b_score':point_b,
                'lack_a':lack_1,
                'lack_b':lack_2,
                'img_sexo':img_sexo,
                'sexo_color': sexo_color,
                'ball_sport': ball_sport,
                'aces_or_card': "Aces",
                'aces_or_card_a': aces_1,
                'aces_or_card_b': aces_2,
                'card_a': card_1,
                'card_b': card_2,
                'aces_a_score': aces_a,
                'aces_b_score': aces_b,
                'sexo_text':match.get_sexo_display(),
                'name_scoreboard': name_scoreboard,
                'photoA': team_1.team.photo.url if team_1.team.photo else default_photo_url,
                'photoB': team_2.team.photo.url if team_2.team.photo else default_photo_url,
                'sets_time_auto': False,
            }
            print("sets on: ",match_data)
            return match_data

    elif Match.objects.filter(status=1):
        match = Match.objects.get(status=1)
        team_matchs = Team_match.objects.filter(match=match)
        team_match_a = team_matchs[0]
        team_match_b = team_matchs[1]
        point_a = Point.objects.filter(team_match=team_match_a).count()
        point_b = Point.objects.filter(team_match=team_match_b).count()
        lack_a = Penalties.objects.filter(type_penalties=2,team_match=team_match_a).count()
        lack_b = Penalties.objects.filter(type_penalties=2,team_match=team_match_b).count()
        card_a = Penalties.objects.filter(type_penalties=0,team_match=team_match_a).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_a).count()
        card_b = Penalties.objects.filter(type_penalties=0,team_match=team_match_b).count() + Penalties.objects.filter(type_penalties=1,team_match=team_match_b).count()
        seconds, status = generate_timer(match)
        if Banner.objects.filter(status=0): 
            banner_score = Banner.objects.get(status=0).image.url
            banner_status_score = True
        else: 
            banner_score = static('images/logo-jifs-intercampi.svg')
            banner_status_score = False
        if match.sexo == 1: 
            img_sexo = static('images/icon-female.svg')
            sexo_color = '#ff32aa' 
        else: 
            img_sexo = static('images/icon-male.svg')
            sexo_color = '#3a7bd5'
        if match.sport == 3:
            ball_sport = static('images/ball-of-handball.png')
        else:
            ball_sport = static('images/ball-of-futsal.png')
        name_scoreboard = 'Tempo'
        match_data = {
            'team_a': team_match_a.team.name,
            'team_b': team_match_b.team.name,
            'team_a_score': team_match_a.team.name,
            'team_b_score': team_match_b.team.name,
            'teamAcolor': team_match_a.team.hexcolor,
            'teamBcolor': team_match_b.team.hexcolor,
            'points_a': point_a,
            'points_b': point_b,
            'lack_a':lack_a,
            'lack_b':lack_b,
            'sets_a': "00:00",
            'sets_b': 0,
            'card_a':card_a,
            'card_b':card_b,
            'banner_score':banner_score,
            'banner_status_score':banner_status_score,
            'points_a_score': point_a,
            'points_b_score': point_b,
            'aces_or_card': "Cartões",
            'aces_or_card_a': card_a,
            'aces_or_card_b': card_b,
            'img_sexo':img_sexo,
            'sexo_color':sexo_color,
            'sexo_text':match.get_sexo_display(),
            'sexo_color':sexo_color,
            'ball_sport':ball_sport,
            'name_scoreboard': name_scoreboard,
            'photoA': team_match_a.team.photo.url if team_match_a.team.photo else default_photo_url,
            'photoB': team_match_b.team.photo.url if team_match_b.team.photo else default_photo_url,
            'seconds':seconds,
            'status':status,
            'sets_time_auto': True,
        }
        return match_data
    else:
        if Banner.objects.filter(status=0): 
            banner_score = Banner.objects.get(status=0).image.url
            banner_status_score = True
        else: 
            banner_score = static('images/logo-jifs-intercampi.svg')
            banner_status_score = False
        match_data = {
            'team_a': "TIME A",
            'team_b': "TIME B",
            'points_a': 0,
            'points_b': 0,
            'aces_or_card': "Cartões",
            'aces_or_card_a':0,
            'aces_or_card_b':0,
            'teamAcolor': '#02007a',
            'teamBcolor': '#d10000',
            'lack_a':0,
            'lack_b':0,
            'sets_a': "00:00",
            'sets_b': 0,
            'card_a':0,
            'card_b':0,
            'name_scoreboard': "PLACAR",
            'photoA': default_photo_url,
            'photoB': default_photo_url,
            'banner_score':banner_score,
            'banner_status_score':banner_status_score,
        }
        return match_data


def send_score_update():
    channel_layer = get_channel_layer()
    match_data = generate_score_data()
    async_to_sync(channel_layer.group_send)(
        'placar',
        {
            'type': 'match_update',
            'match': match_data,
        }
    )

@receiver([post_save, post_delete], sender=Point)
def point_changed(sender, instance, using, **kwargs):
    print("hmm, mudanças nos times :)")
    send_score_update()

@receiver([post_save, post_delete], sender=Time_pause)
def point_changed(sender, instance, using, **kwargs):
    print("hmm, teremos uma pausa ou retorno! :)")
    send_score_update()

@receiver([post_save, post_delete], sender=Match)
def match_updated(sender, instance, using, **kwargs):
    print("hmm, mudanças nas partidas :)")
    send_score_update()

@receiver([post_save, post_delete], sender=Team)
def team_updated(sender, instance, using, **kwargs):
    print("hmm, mudanças nos times :)")
    send_score_update()

@receiver([post_save, post_delete], sender=Penalties)
def penalties_updated(sender, instance, using, **kwargs):
    print("hmm, mudanças nas penalidades :(")
    send_score_update()

@receiver([post_save, post_delete], sender=Volley_match)
def penalties_updated(sender, instance, using, **kwargs):
    print("hmm, mudanças no volley_match :)")
    send_score_update()

@receiver([post_save, post_delete], sender=Banner)
def penalties_updated(sender, instance, using, **kwargs):
    print("hmm, mudanças no volley_match :)")
    send_score_update()

@receiver([post_save, pre_delete], sender=Player_team_sport)
def team_sport_updated(sender, instance, **kwargs):
    validate_team_sport(instance)


def validate_team_sport(instance):
    team_sport = instance.team_sport
    if Player_team_sport.objects.filter(team_sport=team_sport).exists():
        players_numbers = len(Player_team_sport.objects.filter(team_sport=team_sport))
        match team_sport.sport:
            case 1 | 2| 3| 4:
                if players_numbers >= 6 and players_numbers <= 12:
                    team_sport.status = True
                    team_sport.save()
                else:
                    team_sport.status = False
                    team_sport.save()
            case _:
                if players_numbers >= 1 and players_numbers <= 4:
                    team_sport.status = True
                    team_sport.save()
                else:
                    team_sport.status = False
                    team_sport.save()
        print(f"Novo time criado: {instance.player.name}")
    else:
        print(f"Time atualizado: {instance.player.name}")