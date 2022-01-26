from django import forms
from .models import *

#location add form
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = {'location_name','description','image','address'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {'comment','rating'}
