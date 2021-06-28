from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import Link

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)