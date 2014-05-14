from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db import models
import re
#from django.core import Validator
from django.shortcuts import get_object_or_404
from register.models import User
from register.lists import LIST_OF_STATES 
from register.helper import *

GENDER_CHOICES = (('M', 'Male'),('F','Female'))

#Custom Functions
def check_alpha(name):
    if re.match("^[A-Za-z ]*$",name):
        return True
    else:
        return False

def user_exists(username_):
    if Login.objects.all().filter(username=username_):
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
        required=False,
        label='Gender', 
        choices=GENDER_CHOICES, 
        widget=forms.Select()
    )

    address_line_one=forms.CharField(
        required=True,
        label='Address Line One', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Address Line One'}
        )
    )

    address_line_two=forms.CharField(
        required=False,
        label='Address Line Two', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Address Line Two',}
        )
    )

    state=forms.CharField(
        required=False,
        label='State', 
        widget=forms.Select(
            choices=LIST_OF_STATES,    
            attrs={'placeholder': 'State'}, 
        )
    )

    city=forms.CharField(
        required=False,
        label='City', 
        widget=forms.TextInput(
            attrs={'placeholder': 'City'}
        )
    )

    pincode=forms.IntegerField(
        required=False,
        label='Pincode', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Pincode'}
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
    
    position=forms.CharField(
        required=True,
        label='Position', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Position'}
        )
    )

    email=forms.EmailField(
        required=True,
        label='Email', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        )
    )

    class Meta:
        model = User
        widgets = {'user_id':forms.HiddenInput()}

    def clean_name(self):
        name = self.cleaned_data['name']
        if check_alpha(name):
            return name
        else:
            raise forms.ValidationError("Please enter only alphabets")

    def clean_pincode(self):
        pincode = self.cleaned_data['pincode']
        if pincode >110000 and pincode < 930000:
            return pincode
        else:
            raise forms.ValidationError("Please Enter a valid Pincode")
    

