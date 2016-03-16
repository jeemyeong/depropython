# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
import hashlib
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'index.html')

def mail(request):
    name= request.POST['name']
    fromEmail= request.POST['email']
    phone= request.POST['phone']
    message= request.POST['message']

    contents = 'email from '+name+' whose email: '+fromEmail+', phone number: '+phone+'to depromeet :  '+message

    toEmail = 'elvmaks@gmail.com'

    email = EmailMessage('mail from depromeet site', contents, to=[toEmail])
    email.send()

    return HttpResponseRedirect(reverse('home'))

