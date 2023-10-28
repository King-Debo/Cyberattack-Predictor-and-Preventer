# Step 1: Create a Django project and set up the database models, views, and URLs for the website.

# Import the necessary modules
import os
import django
from django.db import models
from django.views import View
from django.http import HttpResponse
from django.urls import path

# Create a Django project named cyberattack
os.system("django-admin startproject cyberattack")

# Change the current directory to the project directory
os.chdir("cyberattack")

# Create a Django app named predictor
os.system("python manage.py startapp predictor")

# Add the app name to the INSTALLED_APPS list in settings.py
with open("cyberattack/settings.py", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace("'django.contrib.staticfiles',", "'django.contrib.staticfiles',\n    'predictor',"))

# Define the database model for storing the cyberattack data
class CyberAttack(models.Model):
    # The fields of the model are based on the data source URL
    # You can modify them according to your needs
    date = models.DateField()
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    impact = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date} {self.country} {self.type}"

# Register the model in admin.py
from django.contrib import admin
from .models import CyberAttack

admin.site.register(CyberAttack)

# Define the view for displaying the home page of the website
class HomeView(View):
    def get(self, request):
        # Return a simple response for now
        # You can modify it later to render a template with the dashboard data
        return HttpResponse("Welcome to the cyberattack predictor website!")

# Define the URL pattern for the home page of the website
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

# Include the app URL patterns in urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("predictor.urls")),
]

# Run the migrations to create the database tables
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

# Run the server to test the website
os.system("python manage.py runserver")
