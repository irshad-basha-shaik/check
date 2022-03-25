from .models import Empower
from django import forms

class EmpowerForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    age = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}),required=False)