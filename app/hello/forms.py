from typing import Text
from django import forms
from django.forms.widgets import TextInput
from .models import Friend, Message


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
        }


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))


class CheckForm(forms.Form):
    required = forms.IntegerField(label='Required',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    min = forms.IntegerField(label='Min', min_value=100,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max = forms.IntegerField(label='Max', max_value=1000,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
            'friend': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }
 