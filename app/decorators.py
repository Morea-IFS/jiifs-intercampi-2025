from functools import wraps
from django.shortcuts import redirect
from datetime import datetime
import pytz
from .models import Settings_access, Terms_Use
from django.contrib import messages

def time_restriction(redirect_page="manage"):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            brasilia_tz = pytz.timezone('America/Sao_Paulo')
            now = datetime.now(brasilia_tz)
            
            config = Settings_access.objects.order_by('-id').first()

            if config:
                if config.start.tzinfo is None:
                    config.start = brasilia_tz.localize(config.start)

            if not config or (config.start <= now <= config.end) or request.user.is_staff:
                print("vaaai")
                return view_func(request, *args, **kwargs)
            else:
                print("euaii")
                messages.info(request, "O período para realizar as inscrições e edições já foi finalizado.")
                return redirect(redirect_page)

        return wrapper
    return decorator

def terms_accept_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        try:
            termo = Terms_Use.objects.get(usuario=request.user)

            if not termo.document:
                return redirect('upload_document')

            if not (termo.name and termo.siape):
                return redirect('boss_data')

            if not termo.accepted:
                return redirect('terms_use')

        except Terms_Use.DoesNotExist:
            return redirect('upload_document')

        return view_func(request, *args, **kwargs)
    
    return wrapper