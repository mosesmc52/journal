# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app import models

# Register your models here.
def register_admin(model):
    """Turn admin.site.register into a decorator."""
    def wrapper(klass):
        admin.site.register(model, klass)
        return klass
    return wrapper

@admin.register(models.journal_submission)
class JournalSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user','created')
    list_filter = ('created',)
    search_fields = ['user']

@admin.register(models.embed)
class EmbedAdmin(admin.ModelAdmin):
    list_display = ('summary','url','source','message')
    list_filter = ('source',)
    search_fields = ['summary']

@admin.register(models.question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','category')
    list_filter = ('category',)
    search_fields = ['question']
