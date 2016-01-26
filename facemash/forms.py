from django import forms
from django.utils.translation import ugettext_lazy as _
import re

class GameForm(forms.Form):
    title = forms.CharField(label = _("Title"), widget = forms.TextInput(attrs=dict(required=True, max_length = 100)))

class FaceMashForm(forms.Form):
    name = forms.CharField(label = _("Title"), widget = forms.TextInput(attrs=dict(required=True, max_length = 10)));
    picture = forms.ImageField();
