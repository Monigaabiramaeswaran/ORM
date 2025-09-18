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


