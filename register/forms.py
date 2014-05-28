from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db import models
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
import re
#from django.core import Validator
from django.shortcuts import get_object_or_404
from register.models import User, Login
from register.lists import LIST_OF_STATES 
from register.helper import *

GENDER_CHOICES = (('M', 'Male'),('F','Female'))
INTEREST_CHOICES = (('Poetry', 'Poetry'), ('Seminar', 'Seminar'))
SKILLS_CHOICES = (('Writing', 'Writing'), ('Web Design', 'Web Design'))

#Custom Functions
def check_alpha(name):
    if re.match("^[A-Za-z ]*$",name):
        return True
    else:
        return False

def user_exists(email_):
    if Login.objects.all().filter(email=email_):
        return True
    else:
        return False

class UserForm(ModelForm):

    name=forms.CharField(
         required=True,
         label='Name', 
         widget=forms.TextInput(
            attrs={'placeholder': 'Name'}
         )
    )

    date_of_birth = forms.DateField(
        required=True,
        widget=DateTimePicker(
            options={
                     "pickTime": False},
            attrs={'placeholder': 'Date of Birth'}
        )
    )

    gender=forms.ChoiceField(
        required=True,
        label='Gender', 
        choices=GENDER_CHOICES, 
        widget=forms.RadioSelect()
    )

    state=forms.CharField(
        required=True,
        label='State', 
        widget=forms.Select(
            choices=LIST_OF_STATES,    
            attrs={'placeholder': 'State'}, 
        )
    )

    city=forms.CharField(
        required=True,
        label='City', 
        widget=forms.TextInput(
            attrs={'placeholder': 'City'}
        )
    )

    contact_no = forms.IntegerField(
        required=True,
        label='Phone number', 
        widget=forms.TextInput(
            attrs={'placeholder':'Phone Number'}
        )
    )

    department=forms.CharField(
        required=True,
        label='Department Name', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Department Name'}
        )
    )
    
    email=forms.EmailField(
        required=True,
        label='Email', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        )
    )

    interest=forms.MultipleChoiceField(
        required=True,
        label='Interests', 
        choices=INTEREST_CHOICES, 
        widget=forms.CheckboxSelectMultiple(
            attrs={'placeholder': 'Interests'}
        )
    )

    skills=forms.MultipleChoiceField(
        required=True,
        label='Skills', 
        choices=SKILLS_CHOICES, 
        widget=forms.CheckboxSelectMultiple(
            attrs={'placeholder': 'Skills'}
        )
    )

    class Meta:
        model = User
        widgets = {'user_id':forms.HiddenInput()}
        exclude = ('usermode')
        usermode = 'Member'

    def clean_name(self):
        name = self.cleaned_data['name']
        if check_alpha(name):
            return name
        else:
            raise forms.ValidationError("Please enter only alphabets")

class LoginForm(ModelForm):

    email=forms.EmailField(
        required=True,
        label='Email', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        )
    )

    password=forms.CharField(
        required=True,
        max_length=100,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    repass = forms.CharField(
        max_length=100,
        required=True,
        label='Re-enter password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Re Enter Your Password'}
        ),
    )


    class Meta:
        model = Login
        widgets = {'password':forms.PasswordInput(),'email':forms.HiddenInput()}

    def clean_repass(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['repass']
        if password == re_password:
            return password
        else:
            raise forms.ValidationError("Passwords don't match")

