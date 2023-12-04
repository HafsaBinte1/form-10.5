from django import forms
from django.forms.widgets import NumberInput
import datetime
# Create your forms here.

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['2000', '2002', '2003']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    FAVORITE_FOODS_CHOICES = [
    ('burger', 'Burger'),
    ('birani', 'Birani'),
    ('pizza', 'Pizza'),
    ]
    favorite_foods = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_FOODS_CHOICES,)