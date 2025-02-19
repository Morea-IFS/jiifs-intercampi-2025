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

def generate_certificates(players, user, t):
    w, h = (1920, 1080)
    buffer = BytesIO() 
    if t == 0:
        for name in players:
            namecertificate = name.player.name.split()[0].upper() + ("_" + name.player.name.split()[1].upper() if len(name.player.name.split()) > 1 else '')
            c = canvas.Canvas(buffer, pagesize=(w, h))
            base_certificate = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_certificate.png') )
            c.drawImage(base_certificate, 0, 0, w, h)
            c.setFont("MsMadi", 100)
            c.drawCentredString(w / 2, h / 2 + 22, name.player.name)
            c.setFont("Outfit", 64)
            c.drawCentredString(540, 260, name.player.get_campus_display().upper())
            signature = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/signature.png') )
            c.drawImage(signature, 1330, 60, 500, 350, mask='auto')
            c.save()
            arquivo_saida = f"CERTIFICADO_{unidecode(namecertificate)}_{name.player.id}.pdf"
            buffer.seek(0)
            certificate = Certificate.objects.create(user=user)
            certificate.name = unidecode(namecertificate)
            certificate.file.save(arquivo_saida, ContentFile(buffer.read()))
            certificate.save()
    else:
        for name in players:
            namecertificate = name.name.split()[0].upper() + ("_" + name.name.split()[1].upper() if len(name.name.split()) > 1 else '')
            c = canvas.Canvas(buffer, pagesize=(w, h))
            base_certificate = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_certificate.png') )
            c.drawImage(base_certificate, 0, 0, w, h)
            c.setFont("MsMadi", 100)
            c.drawCentredString(w / 2, h / 2 + 22, name.name)
            c.setFont("Outfit", 64)
            c.drawCentredString(540, 260, name.get_campus_display().upper())
            signature = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/signature.png') )
            c.drawImage(signature, 1330, 60, 500, 350, mask='auto')
            c.save()
            namebadge = f'CAMPUS_{name.get_campus_display().upper()}_{name.get_type_voluntary_display().upper()}'
            arquivo_saida = f"CRACHA_{unidecode(namebadge)}_{name.id}.pdf"
            buffer.seek(0)
            certificate = Certificate.objects.create(user=user)
            certificate.name = unidecode(namecertificate)
            certificate.file.save(arquivo_saida, ContentFile(buffer.read()))
            certificate.save()

def draw_circular_image(c, image_path, center_x, center_y, diameter):
    img = ImageReader(image_path)
    c.saveState()
    path = c.beginPath()
    path.circle(center_x, center_y, diameter / 2)
    c.clipPath(path, stroke=0, fill=0)
    c.drawImage(
        img,
        center_x - diameter / 2,
        center_y - diameter / 2,
        width=diameter,
        height=diameter,
        mask="auto",
    )
    c.restoreState()
    
def generate_badges(players, user_l, t):
    buffer = BytesIO() 
    if t == '2':
        w, h = A4
        nametag_width = (w - 3 * 20) / 2
        nametag_height = (h - 3 * 20) / 2
        positions = [
            (20, h - 20 - nametag_height),
            (20 * 2 + nametag_width, h - 20 - nametag_height),
            (20, 20),
            (20 * 2 + nametag_width, 20),
        ]
        c = canvas.Canvas(buffer, pagesize=A4)
        for j, user in enumerate(players):
            if j % 4 == 0 and j > 0:
                c.showPage()
            x, y = positions[j % 4]

            c.rect(x, y, nametag_width, nametag_height)
            base_nametag = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_nametag__' + t + '.png'))
            c.drawImage(base_nametag, x, y, width=nametag_width, height=nametag_height)

            if user.player.photo:
                try:
                    photo_diameter = nametag_width / 2 + 20
                    center_x = x + nametag_width / 2
                    center_y = y + nametag_height - photo_diameter + 43
                    draw_circular_image(c, user.player.photo, center_x, center_y, photo_diameter)
                    print(user.player.photo)
                    print(user.player.photo.url)
                except:
                    print("f")

            c.setFont("Helvetica-Bold", 28)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 30,
                (
                    user.player.name.upper()
                    if len(user.player.name) < 15
                    else f"{user.player.name.split()[0].upper()} {next((w[0].upper() + '.' for w in user.player.name.split()[1:] if w.lower() not in ['de', 'da', 'dos', 'das', 'do']), '')}"
                ),
            )

            c.setFont("Helvetica", 18)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 50,
                str(user.player.registration),
            )

            c.setFont("Helvetica-Bold", 18)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 70,
                "CAMPUS: " + user.player.get_campus_display(),
            )

        c.save()
        namebadge = f'CAMPUS_{user.get_campus_display()}_{user.get_type_voluntary_display()}'
        arquivo_saida = f"CRACHA_{unidecode(namebadge)}_{user.id}.pdf"
    else:
        w, h = A4
        nametag_width = (w - 3 * 20) / 2
        nametag_height = (h - 3 * 20) / 2
        positions = [
            (20, h - 20 - nametag_height),
            (20 * 2 + nametag_width, h - 20 - nametag_height),
            (20, 20),
            (20 * 2 + nametag_width, 20),
        ]
        c = canvas.Canvas(buffer, pagesize=A4)
        for j, user in enumerate(players):
            if j % 4 == 0 and j > 0:
                c.showPage()
            x, y = positions[j % 4]

            c.rect(x, y, nametag_width, nametag_height)
            base_nametag = ImageReader( os.path.join(settings.BASE_DIR, 'static/images/generators/base_nametag__' + t + '.png'))
            c.drawImage(base_nametag, x, y, width=nametag_width, height=nametag_height)

            if user.photo:
                try:
                    photo_diameter = nametag_width / 2 + 20
                    center_x = x + nametag_width / 2
                    center_y = y + nametag_height - photo_diameter + 43
                    draw_circular_image(c, user.photo, center_x, center_y, photo_diameter)
                    print(user.photo)
                    print(user.photo.url)
                except:
                    print("f")

            c.setFont("Helvetica-Bold", 28)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 30,
                (
                    user.name.upper()
                    if len(user.name) < 15
                    else f"{user.name.split()[0].upper()} {next((w[0].upper() + '.' for w in user.name.split()[1:] if w.lower() not in ['de', 'da', 'dos', 'das', 'do']), '')}"
                ),
            )

            c.setFont("Helvetica", 18)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 50,
                str(user.registration),
            )

            c.setFont("Helvetica-Bold", 18)
            c.drawCentredString(
                x + nametag_width / 2,
                y + nametag_height / 2 - 70,
                "CAMPUS: " + user.get_campus_display(),
            )

        c.save()
        namebadge = f'CAMPUS_{user.get_campus_display().upper()}_{user.get_type_voluntary_display().upper()}'
        arquivo_saida = f"CRACHA_{unidecode(namebadge)}_{user.id}.pdf"
    buffer.seek(0)
    badge = Badge.objects.create(user=user_l)
    badge.name = namebadge
    badge.file.save(arquivo_saida, ContentFile(buffer.read()))
    badge.save()

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