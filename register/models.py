from django.db import models
from django import forms
GENDER_CHOICES = (('M', 'Male'),('F','Female'))
INTEREST_CHOICES = (('Poetry', 'Poetry'), ('Seminar', 'Seminar'))
SKILLS_CHOICES = (('Writing', 'Writing'), ('Web Design', 'Web Design'))

class User(models.Model):
    name = models.CharField(max_length=100, unique=False)
    date_of_birth = models.DateField(blank=False)
    usermode = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    contact_no = models.CharField(max_length=11)
    department = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True,primary_key=True)
    interest = models.CharField(max_length=200, choices=INTEREST_CHOICES)
    skills = models.CharField(max_length=200, choices=SKILLS_CHOICES)
    date_of_regn = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table= 'ayudh_user'          

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):                     
        return "/users/%s" % self.username

class Login(models.Model):
    email = models.EmailField(unique=True, blank=False, primary_key=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'ayudh_login'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%s" % self.username

