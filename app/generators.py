from io import BytesIO
from django.core.files.base import ContentFile
from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from unidecode import unidecode
from reportlab.pdfbase import pdfmetrics
from django.conf import settings
from reportlab.pdfbase.ttfonts import TTFont
import os, time
from typing import List, Dict
from .models import Badge, Certificate, Match,Events, Match, Time_pause

pdfmetrics.registerFont(TTFont('MsMadi', 'fonts/MsMadi-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Outfit', 'fonts/Outfit-Black.ttf'))

def generate_certificates(players, user):
    w, h = (1920, 1080)
    buffer = BytesIO() 

    for name in players:
        namecertificate = name.player.name.split()[0].upper() + ("_" + name.player.name.split()[1].upper() if len(name.player.name.split()) > 1 else '')
        c = canvas.Canvas(buffer, pagesize=(w, h))
        base_certificate = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_certificate.png') )
        c.drawImage(base_certificate, 0, 0, w, h)
        c.setFont("MsMadi", 100)
        c.drawCentredString(w / 2, h / 2 + 22, name.player.name)
        c.setFont("Outfit", 64)
        c.drawCentredString(540, 260, name.player.campus.upper())
        signature = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/signature.png') )
        c.drawImage(signature, 1330, 60, 500, 350, mask='auto')
        c.save()
        arquivo_saida = f"CERTIFICADO_{unidecode(namecertificate)}_{name.player.id}.pdf"
        buffer.seek(0)
        certificate = Certificate.objects.create(user=user)
        certificate.name = unidecode(namecertificate)
        certificate.file.save(arquivo_saida, ContentFile(buffer.read()))
        certificate.save()


def generate_badges(players, user):
    buffer = BytesIO() 
    c = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4
    nametag_width = (w - 3 * 20) / 2
    nametag_height = (h - 3 * 20) / 2
    positions = [
        (20, h - 20 - nametag_height),
        (20 * 2 + nametag_width, h - 20 - nametag_height),
        (20, 20),
        (20 * 2 + nametag_width, 20)
    ]
    for j, i in enumerate(players):
        print("j: ",j, "i: ",i.player.name, " : ",i)
        if j % 4 == 0 and j > 0:
            c.showPage()
        x, y = positions[j % 4]

        c.rect(x, y, nametag_width, nametag_height)
        s = str(2)
        base_nametag = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_nametag__' + s + '.png'))
        c.drawImage(base_nametag, x, y, width=nametag_width, height=nametag_height)
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(
            x + nametag_width / 2, 
            y + nametag_height / 2 - 30, 
            i.player.name.upper() if len(i.player.name) < 15 else f"{i.player.name.split()[0].upper()} {next((w[0].upper() + '.' for w in i.player.name.split()[1:] if w.lower() not in ['de', 'da', 'dos', 'das', 'do']), '')}"
        )
    c.save()
    buffer.seek(0)
    badge = Badge.objects.create(user=user)
    badge.name = f'nametags__{badge.id}'
    arquivo_saida = f'nametags__{badge.id}.pdf'
    badge.file.save(arquivo_saida, ContentFile(buffer.read()))
    badge.save()

    return badge


def generate_events(name, details):
    match = Match.objects.get(status=1)
    Events.objects.create(name=name,details=details, match=match)


def generate_timer(match):
    rel = time.localtime()
    seconds = 0
    if match.time_start and match.time_end:
        seconds = (match.time_end.hour * 60 * 60 + match.time_end.minute * 60 + match.time_end.second) - (match.time_start.hour * 60 * 60 + match.time_start.minute * 60 + match.time_start.second)
        status = 3
        if Time_pause.objects.filter(match=match):
            pausas_totais = Time_pause.objects.filter(match=match)
            somatorio = 0
            for i in pausas_totais: somatorio += (i.end_pause.hour * 60 * 60 + i.end_pause.minute * 60 + i.end_pause.second) - (i.start_pause.hour * 60 * 60 + i.start_pause.minute * 60 + i.start_pause.second)
            seconds -= somatorio
            print(seconds)
    elif match.time_start:
        print("kk: ",seconds)
        if Time_pause.objects.filter(match=match):
            seconds = (rel.tm_hour * 60 * 60 + rel.tm_min * 60 + rel.tm_sec) - (match.time_start.hour * 60 * 60 + match.time_start.minute * 60 + match.time_start.second)
            pause = Time_pause.objects.filter(match=match).last()
            pausas_totais = Time_pause.objects.filter(match=match)
            somatorio = 0
            if pause.start_pause and pause.end_pause:
                print("Entrou no pausa finalizada jogo continua")
                status = 1
                for i in pausas_totais:
                    print(i.end_pause,i.start_pause)
                    somatorio += (i.end_pause.hour * 60 * 60 + i.end_pause.minute * 60 + i.end_pause.second) - (i.start_pause.hour * 60 * 60 + i.start_pause.minute * 60 + i.start_pause.second)
                    print(somatorio)
                seconds -= somatorio
            elif pause.start_pause and not pause.end_pause and Time_pause.objects.filter(match=match).count() > 1:
                seconds = (pause.start_pause.hour * 60 * 60 + pause.start_pause.minute * 60 + pause.start_pause.second) - (match.time_start.hour * 60 * 60 + match.time_start.minute * 60 + match.time_start.second)        
                print("Entrou no pausa iniciada não é a primeira")
                print("g:",seconds)
                status = 2
                for i in pausas_totais:
                    if i == pausas_totais.last():
                        break
                    somatorio += (i.end_pause.hour * 60 * 60 + i.end_pause.minute * 60 + i.end_pause.second) - (i.start_pause.hour * 60 * 60 + i.start_pause.minute * 60 + i.start_pause.second)
                seconds -= somatorio
            elif pause.start_pause and not pause.end_pause:
                print("Entrou no pausa iniciada, a primeira")
                status = 2
                seconds = (pause.start_pause.hour * 60 * 60 + pause.start_pause.minute * 60 + pause.start_pause.second) - (match.time_start.hour * 60 * 60 + match.time_start.minute * 60 + match.time_start.second)
        else:
            status = 1
            seconds = (rel.tm_hour * 60 * 60 + rel.tm_min * 60 + rel.tm_sec) - (match.time_start.hour * 60 * 60 + match.time_start.minute * 60 + match.time_start.second)
    else:
        seconds = 0
        status = 0
    print("Tempo: ",seconds, " status: ",status)
    return seconds, status