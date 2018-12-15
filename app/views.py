# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate,login, logout
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.shortcuts import render
from app import forms
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from annoying.functions import get_object_or_None
from django.contrib.sites.models import Site

from app import models
# Create your views here.

def signin(request):

    if request.method == 'POST':
        form = forms.SignIn(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user, backend='backend.email-auth.EmailBackend')
            return redirect('compose')

    resp_dic = {'form': forms.SignIn()}
    return render(request, 'sign-in.html' , resp_dic)

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=email, password=raw_password)

            message = render_to_string('./email/welcome.html', {
                'user': user,
            })
            user.email_user('Welcome to Journal', message)

            login(request, user, backend='backend.email-auth.EmailBackend')
            return redirect('compose')

    resp_dic = {'form': forms.SignUpForm() }
    return render(request, 'sign-up.html' , resp_dic)

def signout(request):
    # logout user
	logout(request);
	return redirect('signin')

def forgot(request):
    if request.method == 'POST': # If the form has been submitted...
    	form = forms.ForgotPassword(request.POST)
        if form.is_valid():
            user = get_object_or_None(models.User, email = form.cleaned_data['email'])

            # send user forgot password email
            message = render_to_string('./email/forgot.html', {
                'user': user,
            			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            			'token': default_token_generator.make_token(user),
                        'site_url':Site.objects.get_current().domain,
            })
            user.email_user('Forgot your password, Oh my!', message)

            if user:
              	return redirect('signin')

    resp_dic = {'form': forms.ForgotPassword}
    return render(request, 'forgot-password.html' , resp_dic)

def forgot_change(request, uidb64, token):

    resp_dic = {}

    if request.method == 'POST': # If the form has been submitted...
        form = forms.ChangePassword(request.POST)

        if form.is_valid():

            uid = urlsafe_base64_decode(uidb64)
            user = get_object_or_None(models.User, pk = uid)

            if user and default_token_generator.check_token(user, token):
                new_password= form.cleaned_data['password1']
                user.set_password(new_password)
                user.save()

                # login
                auth = authenticate(username=user.email.strip().lower(), password=new_password)
                login(request, auth, backend='backend.email-auth.EmailBackend')

                return redirect('compose')
            else:
                return redirect('forgot')

    resp_dic = {'token': token, 'uid': uidb64, 'form': forms.ChangePassword()}

    return render(request, 'forgot-change-password.html' , resp_dic)

def compose_entry(request, uidb64 = None, token = None):

    if uidb64:
        uid = urlsafe_base64_decode(uidb64)
        user = get_object_or_None(models.User, pk = uid)
        if user and default_token_generator.check_token(user, token):
            pass
        else:
            return redirect('signin')

    if request.method == 'POST':    # check if form has been submitted
        form = forms.JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submitted')

    if models.journal_submission.objects.filter( user = request.user).count():
        lastpost = models.journal_submission.objects.filter( user = request.user).latest('created').created
    else:
        lastpost = None

    resp_dic = {'today': datetime.today(), 'lastpost': lastpost,
                'form': forms.JournalEntryForm(initial={'user': request.user.pk }),
                'question':models.question.objects.all().order_by('?')[:1].get()}
    return render(request, 'compose.html' , resp_dic)

def entry_submitted(request):
    resp_dic = {'embed': models.embed.objects.all().order_by('?')[:1].get()}
    return render(request, 'entry_submited.html' , resp_dic)
