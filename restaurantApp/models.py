from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_detail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact=models.IntegerField(null=True)
 
    def __str__(self):
        return self.user.username

TABLE_CHOICES = (
    ('Table of 2 Guest','Table of 2 Guest'),
    ('Table of 3 Guest','Table of 3 Guest'),
    ('Table of 4 Guest','Table of 4 Guest'),
    ('Table of 5 Guest','Table of 5 Guest'),
    ('Table of 6 guest','Table of 6 Guest'),
)
PORPOSE_CHOICES = (
    ('Meeting','Meeting'),
    ('Casual','Casual'),
    ('Celebration','Celebration'),
)

PLAN_CHOICES = (
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
)

class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="Reservations")
    typeoftable=models.CharField(max_length=50,choices=TABLE_CHOICES,null=True)
    purpose=models.CharField(max_length=50,choices=PORPOSE_CHOICES,null=True)
    mealplan=models.CharField(max_length=40,choices=PLAN_CHOICES,null=True)
    arrivaltime=models.TimeField(max_length=30,null=True)
    bookdate=models.DateField(max_length=40,null=True)
    # status=models.CharField(max_length=50,null=True)
    # amount = models.IntegerField(null=True)
    
    def __str__(self):
        return self.purpose
        pass
        #return self.user.username

class Menu(models.Model):
    APPETIZERS = 'Appetizers'
    SNACKS = 'Snacks'
    SOUPSandSALADS ='Soups & Salads'
    PIZZAS = 'Pizzas'
    SANDWICHES = 'Sandwiches'
    STEAKSandSEAFOOD = 'Steaks & Seafood'
    DESSERTS = 'Desserts'
    DRINKS = 'Drinks'

    Meal_CATEGORIES = [
        (APPETIZERS, 'Appetizers'),
        (SNACKS, 'Snacks'),
        (SOUPSandSALADS, 'Soups & Salads'),
        (PIZZAS, 'Pizzas'),
        (SANDWICHES, 'Sandwiches'),
        (STEAKSandSEAFOOD, 'Steaks & Seafood'),
        (DESSERTS, 'Desserts'),
        (DRINKS, 'Drinks'),
    ]

    mealPicture = models.TextField()
    mealName = models.CharField(max_length=50)
    mealDescription = models.CharField(max_length=250)
    category = models.CharField(max_length=20, choices=Meal_CATEGORIES, default='All')
    calories = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.mealName

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="comments")
    title=models.CharField(max_length=50)
    body=models.TextField()
    date_added = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title