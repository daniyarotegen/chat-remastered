from django import forms
from django.contrib.auth.models import User


class GroupChatForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
