from django.urls import path 
from . import views

urlpatterns = [
 path("", views.ApiOverview, name="home"),
 path("create/", views.add_items, name="add-items"),
 path("email/", views.sendEmail, name="send-email")
]
