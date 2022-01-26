import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Location
from .models import Review
from django.urls import reverse

'''***************************************************************************************
*  REFERENCES
*
*  1)
*  Title: datetime tests and setup from "Writing your first Django app, part 5"
*  Author: Django Documentation
*  URL: https://docs.djangoproject.com/en/3.2/intro/tutorial05/
***************************************************************************************'''


def create_location(name,desc,avg_rat,adrs):
    return Location.objects.create(location_name=name,description=desc,averageRating=avg_rat,address=adrs)

class LocationTestCase(TestCase):
    def setUp(self):
        self.loc = create_location("test","this is a test function",6.7,"332 fake ave")
    def test_render(self):
        response = self.client.get('/reviews/')
        self.assertTemplateUsed(response, 'reviews/index.html')
    def test_loc_exists(self):
        loc_obj = Location.objects.get(location_name="test")
        self.assertTrue(loc_obj)
    def test_fakeloc_doesntexist(self):
        # trys to get fake object, if an error happens the test passes otherwise it fails
        try:
            Location.objects.get(location_name="not real")
            self.assertTrue(False)
        except:
            self.assertTrue(True)
    def test_loc_fields_description(self):
        loc_obj = Location.objects.get(location_name="test")
        desc = loc_obj.description
        self.assertEqual(desc,"this is a test function")
    
    def test_loc_fields_averageRating(self):
        loc_obj = Location.objects.get(location_name="test")
        avg_rat = loc_obj.averageRating
        self.assertEqual(avg_rat,6.7)   

    def test_loc_fields_address(self):
        loc_obj = Location.objects.get(location_name="test")
        adrs = loc_obj.address
        self.assertEqual(adrs,"332 fake ave")   
def create_review(loc, com, rat):
    return Review.objects.create(location = loc, comment = com, rating= rat)
class ReviewTestCase(TestCase):
    def setUp(self):
        self.loc = create_location("test","this is a test function",6.7,"332 fake ave")
        self.rev = create_review(self.loc,"this is a test review",5.5)
    def test_render(self):
        response = self.client.get('/reviews/')
        self.assertTemplateUsed(response, 'reviews/index.html')
    def test_rev_exists(self):
        rev_obj = Review.objects.get(location=self.loc)
        self.assertTrue(rev_obj)
    def test_rev_doesntexist(self):
        self.loc2 = create_location("test","this is a test function",6.7,"332 fake ave")
        # trys to get fake object, if an error happens the test passes otherwise it fails
        try:
            Review.objects.get(location=self.loc2)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
    def test_rev_fields_comment(self):
        rev_obj = Review.objects.get(location=self.loc)
        com = rev_obj.comment
        self.assertEqual(com,"this is a test review")

    def test_rev_fields_rating(self):
        rev_obj = Review.objects.get(location=self.loc)
        rat = rev_obj.rating
        self.assertEqual(rat,5.5)

def create_review2(loc, com, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Review.objects.create(location = loc, comment = com, pub_date = time)


#test cases for Datetimes from https://docs.djangoproject.com/en/3.2/intro/tutorial05/,
#which is the Django Practice Assessment tutorial. (reference #1)
class ReviewTestDateTimes(TestCase):
    def test_was_published_recently_with_future_review(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_review = Review(pub_date=time)
        self.assertIs(future_review.was_published_recently(), False)
    def test_was_published_recently_with_old_review(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_review = Review(pub_date=time)
        self.assertIs(old_review.was_published_recently(), False)

    def test_was_published_recently_with_recent_review(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_review = Review(pub_date=time)
        self.assertIs(recent_review.was_published_recently(), True)