from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('home' , views.login, name = "home_public"),
    path('placar' , views.scoreboard_public, name="scoreboard_public"),
    path('scoreboard_projector', views.scoreboard_projector, name="scoreboard_projector"),
    path('sobre', views.about_us, name="about_us"),
    path('login' , views.login, name = "login"),
    path('logout', views.sair, name='logout'),
    path('', views.home_admin, name = "Home"),
    path('manage/player', views.player_manage, name = "player_manage"),
    path('edit/player/<int:id>', views.player_edit, name = "player_edit"),
    path('manage/team', views.team_manage, name = "team_manage"),
    path('edit/team/<int:id>', views.team_edit, name = "team_edit"),
    path('manage/player/team/<int:id>', views.team_players_manage, name = "team_players_manage"),
    path('manage/match', views.matches_manage, name = "matches_manage"),
    path('edit/match/<int:id>', views.matches_edit, name = "matches_edit"),
    path('add/player/team/<int:id>', views.add_player_team, name = "add_player_team"),
    path('register/match', views.matches_register, name = "matches_register"),
    path('games', views.games, name = "games"),
    path('attachments', views.attachments, name = "attachments"),
    path('manage/technician', views.technician_manage, name = "technician_manage"),
    path('register/technician', views.technician_register, name = "technician_register"),
    path('edit/technician/<int:id>', views.technician_edit, name = "technician_edit"),
    path('register/voluntary', views.voluntary_register, name = "voluntary_register"),
    path('manage/voluntary', views.voluntary_manage, name = "voluntary_manage"),
    path('edit/voluntary/<int:id>', views.voluntary_edit, name = "voluntary_edit"),
    path('general/data/<int:id>', views.general_data, name = "general_data"),
    path('scoreboard', views.scoreboard, name = "scoreboard"),
    path('manage/projector', views.projector_manage, name="projector_manage"),
    path('register/projector', views.projector_register, name="projector_register"),
    path('manage/banner', views.banner_manage, name="banner_manage"),
    path('register/banner', views.banner_register, name="banner_register"),
    path('players_match/<int:id>', views.players_match, name = "players_match"),
    path('players_in_teams/<int:id>', views.players_in_teams, name = "players_in_teams"),
    path('timer/<int:id>', views.timer_page, name = "timer"),
    path('upload/', views.upload_document, name='upload_document'),
    path('dados/', views.boss_data, name='boss_data'),
    path('termos/', views.terms_use, name='terms_use'),
    path('erro404', views.page_in_erro404),
    path('manage', views.manage, name="manage"),
    path('settings', views.settings, name="settings"),

    path('chefe_manage', views.chefe_manage, name="chefe_manage"),
    path('faq_manage', views.faq_manage, name="faq_manage"),
    path('faq_register', views.faq_register, name="faq_register"),
    path('enrollment_manage', views.enrollment_manage, name="enrollment_manage"),
    path('enrollment_register', views.enrollment_register, name="enrollment_register"),
    path('anexo_manage', views.anexo_manage, name="anexo_manage"),
    path('anexo_register', views.anexo_register, name="anexo_register"),

    path('register_team', views.register_team, name="guiate_register_team"),
    path('team/<str:sport_name>', views.team_sexo, name="guiate_team"),
    path('players/<str:team_name>/<str:team_sexo>/<str:sport_name>', views.players_team, name="guiate_players_team"),
    path('players/<str:team_name>/list/<str:team_sexo>/<str:sport_name>/', views.players_list, name="guiate_players_list"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('generator/badge', views.generator_badge, name="badge"),
    path('generator/certificate', views.generator_certificate, name="certificate"),
    path('generator/data', views.generator_data, name="data"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    path('manage/sport', views.sport_manage, name = "sport_manage"),
    path('register/sport', views.sport_register, name = "sport_register"),
    path('edit/sport/<int:id>', views.sport_edit, name = "sport_edit"),
    path('add_players_match/<int:id>', views.add_players_match, name = "add_players_match"),
"""