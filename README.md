# Ex02 Django ORM Web Application
## Date: 15.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Car(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    color=models.CharField(max_length=10)
    year=models.IntegerField()
    rating=models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display=('cid','cname','color','year','rating')

admin.py
from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)
```


## OUTPUT

![alt text](<Screenshot (23).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
