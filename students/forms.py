from django import forms
from . models import Studentprofile

class Studentsforms(forms.ModelForm):
    class Meta:
        model = Studentprofile
        fields = "__all__"