import uuid
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

def send_login_email(request):
    email = request.POST['email']
    uid = str(uuid.uuid4())
    url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
    send_mail(
        'Your login link for Superlists',
        f'Use this link to log in:\n\n{url}',
        'noreply@superlists',
        [email]        
    )

    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    return redirect('/')
