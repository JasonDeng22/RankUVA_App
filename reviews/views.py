from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Location#, Thoughts
from django.urls import reverse_lazy
from django.views import generic
from django.forms import modelformset_factory
from django.views.generic import CreateView 
from .forms import *
from django.db.models import Avg
app_name = "reviews"

'''***************************************************************************************
*  REFERENCES
*
*  1)
*  Title: Django shortcut functions
*  Author: Django Documentation
*  URL: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/
*  Comment: Documentation on HTTP functions like render(),request(),context, etc. 
*  2)
*  Title: Models 
*  URL: https://docs.djangoproject.com/en/3.2/topics/db/models/
*  Comment: Documentation on models and how to work with model specific IDs. 
*  3)
*  Title: Django Tutorial Part 9: Working with forms
*  URL: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
*  Comment: Tutorial that I used to help write forms in views.py. This helped with 
*           stuff like how to use render, request, context, etc. 
*  
***************************************************************************************'''

def home(request):
    query = request.GET.get("title")
    allLocations = None
    if query:
        allLocations = Location.objects.filter(location_name__icontains=query)
    else:
        allLocations = Location.objects.all()

    context = {
        "locations": allLocations,
    }

    return render(request, 'reviews/index.html', context)

#detail page for specific location id
def detail(request, id):
    location = Location.objects.get(id = id)
    reviews = Review.objects.filter(location=id).order_by("-pub_date")

    average = reviews.aggregate(Avg("rating"))['rating__avg']
    if average==None:
        average = 0
    average = round(average,2)

    context = {
        "location": location,
        "reviews": reviews,
        "average": average,
    }
    return render(request, 'reviews/details.html', context)

def add_review(request, id):
    location = Location.objects.get(id=id) 
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            comment = request.POST["comment"]
            rating = request.POST["rating"]
            location = location
            newReviewForm = Review(location=location, firstname =request.user.first_name, 
                                   lastname=request.user.last_name, email = request.user.email,
                                   comment = comment, rating = rating)
            newReviewForm.save()
            return redirect("reviews:detail",id) 
    else:
        form = ReviewForm()
    return render(request,'reviews/details.html',{"form": form})

def edit_review(request, location_id, review_id):
    if request.user.is_authenticated:
        location = Location.objects.get(id = location_id)
        review = Review.objects.get(location = location, id = review_id)
        #check if review was made by the current user. This is done by checking if the current user's email address
        #is the same as the email address saved for the review. This should be relatively secure since gmail does not
        #let people have the same email address
        if request.user.email == review.email:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance = review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out of range. Please select rating from 0 to 10."
                        return render(request,'reviews/editreview.html', {"error":error, "form":form})
                    elif ( data.rating not in [0,1,2,3,4,5,6,7,8,9,10]):
                        error = "Please enter in a whole number from 0-10. No decimals!"
                        return render(request,'reviews/editreview.html', {"error":error, "form":form})
                    else:
                        data.save()
                    return redirect("reviews:detail",location_id)
            else:
                form = ReviewForm(instance = review)
            return render(request,'reviews/editreview.html', {"form": form})
        else:
            return redirect("revies:detail",location_id)
    else:
        return "something's supposed to be here, but I don't know what..."

def delete_review(request, location_id, review_id):
    if request.user.is_authenticated:
        location = Location.objects.get(id = location_id)
        review = Review.objects.get(location = location, id = review_id)
        #check if review was made by the current user
        if request.user.email == review.email:
            # grant permission to delete
            review.delete()
  
        return redirect("reviews:detail",location_id)
    else:
        return "something's supposed to be here, but I don't know what..."
def map(request):
    return render(request,'reviews/map.html')
        
