from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.map,name='map'),
    path('reviews/', views.home, name='index'), #view list of locations
    path('details/<int:id>/',views.detail,name="detail"),
    path('addreview/<int:id>/',views.add_review,name="add_review"),
    path('editreview/<int:location_id>/<int:review_id>/',views.edit_review,name="edit_review"),
    path('deletereview/<int:location_id>/<int:review_id>/',views.delete_review,name="delete_review"),
]