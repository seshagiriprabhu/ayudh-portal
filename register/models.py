from django.db import models
from django import forms
GENDER_CHOICES = (('M', 'Male'),('F','Female'))

class User(models.Model):
        name = models.CharField(max_length=100, unique=False)
        date_of_birth = models.DateField(blank=False)
        gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
        address_line_one = models.CharField(max_length=50, blank=False)
        address_line_two = models.CharField(max_length=50, null=True)
        state = models.CharField(max_length=30, blank=False)
        city = models.CharField(max_length=30, blank=False)
        pincode = models.IntegerField()
        contact_no = models.CharField(max_length=11)
        department = models.CharField(max_length=150, blank=False)
        position = models.CharField(max_length=50, blank = False)
        email = models.EmailField(blank=False, unique=True,primary_key=True)
        class Meta:
                db_table= 'ayudh_user'          

        def __unicode__(self):
                return self.email

        def get_absolute_url(self):                     
                return "/users/%s" % self.username

