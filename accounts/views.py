from django.core.mail import send_mail
from django.shortcuts import render, redirect

def send_login_email(request):
    email = request.POST['email']
    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email]        
    )
    return redirect('/')
