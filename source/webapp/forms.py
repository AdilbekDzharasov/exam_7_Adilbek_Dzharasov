from django import forms
from django.forms import widgets


class EntryForm(forms.Form):
    name = forms.CharField(max_length=300, required=True, label='Name')
    email = forms.EmailField(max_length=300, required=True, label='Email')
    text_entry = forms.CharField(max_length=4000, required=True, label='Text entry', widget=widgets.Textarea)

