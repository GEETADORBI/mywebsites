from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
class Weather(forms.Form):
    temp=forms.CharField(label='temprature',max_length=30)
