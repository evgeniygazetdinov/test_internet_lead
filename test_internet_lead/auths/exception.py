# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.models import User

def check_email_exists(request, backend, details, uid, user=None, *args, **kwargs):
    email = details.get('email', '')
    provider = backend.name

    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    exists = User.objects.filter(username=email).exists()

    if not user and not social and not exists:
        messages.info(request, 'Аккаунт не существует. Пожалуйста, обратитесь к администратору')
