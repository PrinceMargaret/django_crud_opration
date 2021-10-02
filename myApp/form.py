from django import forms
from .models import Person
class nameForm(forms.ModelForm):
   
    
    class Meta:
        model = Person
        fields = ['fname', 'lname']