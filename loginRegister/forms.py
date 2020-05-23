from django import forms

class category(forms.Form):
    Title = forms.CharField(max_length=50, widget=forms.TextInput)
    Description = forms.CharField(max_length=2048, widget=forms.TextInput)

class db_category(forms.Form):
    Title = forms.CharField(max_length=50, widget=forms.TextInput)
    Description = forms.CharField(max_length=2048, widget=forms.TextInput)
    Category = forms.CharField(max_length=50, widget=forms.TextInput)