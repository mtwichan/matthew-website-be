from django import forms
from martor.fields import MartorFormField

class ProjectForm(forms.ModelForm):
    content = MartorFormField()