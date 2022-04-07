from django import forms
from django.utils.translation import gettext_lazy as _


class ContactEmailForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'placeholder': _('Name'), 'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': _('Email'), 'class': 'form-control'}))
    subject = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={'placeholder': _('Subject'), 'class': 'form-control'}))
    text = forms.CharField(max_length=255,
                           widget=forms.Textarea(
                               attrs={'placeholder': _('Enter your message'), 'class': 'form-control'}))
