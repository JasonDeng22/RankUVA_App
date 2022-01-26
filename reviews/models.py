import datetime
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

'''***************************************************************************************
*  REFERENCES
*
*  1)
*  Title: datetime tests and setup from "Writing your first Django app, part 5"
*  Author: Django Documentation
*  URL: https://docs.djangoproject.com/en/3.2/intro/tutorial05/
*
*  2)
*  Title: "How to Display Only the Date from a DateTimeField Object in Django"
*  Author: Learning about Electronics
*  URL: http://www.learningaboutelectronics.com/Articles/How-to-display-only-the-date-from-a-DateTimeField-object-in-Django.php
*  
*  3)
*  Title: Model field reference
*  Author: Django Documentation
*  URL: https://docs.djangoproject.com/en/3.2/ref/models/fields/
***************************************************************************************'''


#each location will have a name, average rating, description, image and address attached to it.

class Location(models.Model):
    location_name = models.CharField(max_length=1000)
    averageRating = models.FloatField(default=0)
    description = models.TextField(max_length=5000)
    #The information on fields (specifically the code for URLField) was taken from reference #3
    image = models.URLField(default=None, null=True)
    address = models.CharField(max_length=1000,default=None,null=True)
    def __str__(self):
        return self.location_name
    
#each review will be tied to a location. the firstname, lastname, and email fields will be taken directly
#from the user's google account information. the first name and last name will automatically be displayed
#with each review, and the email will not be displayed but will be used to verify users when trying to 
#edit or delete a review. 
class Review(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    firstname =  models.CharField(max_length=1000,default=None,null=True)
    lastname = models.CharField(max_length=1000,default=None,null=True)
    email = models.CharField(max_length=1000,default=None,null=True)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published',auto_now_add=True,null=True)
    def __str__(self):
        return self.location.location_name

    #was_published_recently code was taken from reference #1. this code is to help test the dates/times. 
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    #strftime code was taken from reference #2. This code is to help truncate original datetime strings, which
    #would show the entire date including seconds, minutes, hours. This removes that so it's only M-D-Y. 
    def datepublished(self):
        return self.pub_date.strftime('%B %d %Y')