from django import forms
from django.contrib.auth.forms import (
        UserCreationForm,
        AuthenticationForm
        )
from django.contrib.auth.models import User

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from annoying.functions import get_object_or_None

from app import models

class JournalEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JournalEntryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.journal_submission
        fields = ('user','entry')
        widgets = {
            'user': forms.HiddenInput(),
            'entry': SummernoteWidget(attrs={'toolbar': [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['Insert',['picture','link']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['Misc',['fullscreen','undo','redo']]
            ],'width': '100%','height': '380',})
        }

class SignIn(forms.Form):
    email  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email','parsley-type':'email','parsley-trigger':'change'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    #remember_me = forms.BooleanField(label="Remember Me", initial=False)
    def __init__(self, *args, **kwargs):
        super(SignIn, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

class ForgotPassword(forms.Form):
    email  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email','parsley-type':'email','parsley-trigger':'change'}))
    def __init__(self, *args, **kwargs):
        super(ForgotPassword, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

class ChangePassword(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'pass1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm','data-parsley-equalto':'#pass1'}))

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
    email  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email','parsley-type':'email','parsley-trigger':'change'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'pass1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm','data-parsley-equalto':'#pass1'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',  'password1', 'password2', )

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Your Email','type':'email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'})
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
