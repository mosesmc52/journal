# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import EncryptedTextField
from choice import  (
    EMBED_SOURCE,
    QUESTION_CATEGORY
)

# Create your models here.

class journal_submission(models.Model):
    user = models.OneToOneField(User,null=True, blank=True)
    entry = EncryptedTextField()
    created = models.DateTimeField( auto_now_add=True)
    last_sent = models.DateTimeField( auto_now = True)
    def __unicode__(self):
        return ''

class question(models.Model):
    category = models.CharField(max_length=255,blank=True, null=True, choices=QUESTION_CATEGORY)
    question = models.CharField(max_length=255,blank=True, null=True)
    def __unicode__(self):
        return self.question

class embed(models.Model):
    summary =  models.CharField(max_length=255,blank=True, null=True)
    message = models.CharField(max_length=255,blank=True, null=True)
    source = models.CharField(max_length=255,blank=True, null=True, choices=EMBED_SOURCE)
    url = models.CharField(max_length=255,blank=True, null=True)



    def __unicode__(self):
        return self.summary
