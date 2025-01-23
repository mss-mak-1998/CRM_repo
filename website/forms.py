from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Record

#LOGIN FORM
class LoginForm(forms.Form):
    
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
    }))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
    }))


#REGISTRATION FORM
class RegistrationModelForm(UserCreationForm):
    email = forms.EmailField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        'placeholder': 'Josh.Landers@gmail.com'
    }))
    
    first_name = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        'placeholder': 'Gopolang'
    }))
    
    last_name = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        'placeholder': 'Makgothi'
    }))
    
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        'placeholder': 'The name you will use on the app Eg. SydMakgothi'
    }))
    
   
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    
#CREATE RECORDS FORM 

class RecordModelForm(forms.ModelForm):
#FORMATTING SECTION

    first_name = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        
    }))
     
    last_name = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
       
    }))
    
    age = forms.IntegerField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        
    }))
    
    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
    }))
    
    country = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
    }))
    
    city = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
    }))
    
    zip_code = forms.CharField(widget = forms.TextInput(attrs = {
        'class': 'form-control', #Form control helps us style our form with Bootstrap
        'placeholder': '20047'
    }))
    
    
    #FEILD CREATION SECTION
    
    class Meta:
        model = Record
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'country',
            'city',
            'zip_code'
        ]