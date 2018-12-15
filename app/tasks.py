from datetime import datetime, timedelta

from django.db import connection
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
import celery
from journal.celery import app
from annoying.functions import get_object_or_None

from app import models

class FaultTolerantTask(celery.Task):
    """ Implements after return hook to close the invalid connection.
    This way, django is forced to serve a new connection for the next
    task.
    """
    abstract = True

    def after_return(self, *args, **kwargs):
        connection.close()

@app.task(base=FaultTolerantTask)
def reminder():
    today = datetime.now()
    for user in models.User.objects.all():

        # if 1, message 1
        if models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 1)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
        # elif 7, message 2
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 7)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
            # elif 14, message 3
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 14)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
            # elif 30, message 4
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 30)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
            # elif 60, message 5
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 60)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
            # elif 180, message 6
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 180)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass
            # elif 360, message 7
        elif models.journal_submission.objects.filter(user=user, created__startswith = (today - timedelta( days = 360)).date()).count():
            #message = render_to_string('./email/welcome.html', {
            #    'user': user,
            #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #			'token': default_token_generator.make_token(user)
            #           'site_url':Site.objects.get_current().domain,
            #})
            pass

        #user.email_user(subject, message)

@app.task(base=FaultTolerantTask)
def memory_lane():
    # todays date
    today = datetime.now()
    today = datetime.now()
    for user in models.User.objects.all():
        #check if user posted 1 year
        if models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 365)).date()).count():
            submission = models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 365)).date()).order_by('?')[:1].get()
        #check if user posted 6 months
        elif models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 180)).date()).count():
            submission = models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 180)).date()).order_by('?')[:1].get()
        #check if user posted 3 months
        elif models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 90)).date()).count():
            submission = models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 90)).date()).order_by('?')[:1].get()
        # check if user posted 1 month ago
        elif models.journal_submission.objects.filter(user=user, created__lte = (today - timedelta( days = 30)).date()).count():
            submission = models.journal_submission.objects.filter( user=user,created__lte = (today - timedelta( days = 30)).date()).order_by('?')[:1].get()

        # search for random post on that day

        #message = render_to_string('./email/welcome.html', {
        #    'user': user,
        #			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #			'token': default_token_generator.make_token(user)
        #           'site_url':Site.objects.get_current().domain,
        #})
        #user.email_user(subject, message)

        # save to keep trace of last time submission was updated
        submission.save()
