from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Reservations , Comment
from django.core.exceptions import ValidationError
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields = ['username' , 'first_name' , 'last_name' , 'email' ]
        labels= {'email' : 'Email'}
class ReservationForm(forms.ModelForm):
    

    class Meta:
        model = Reservations
        labels= {
            'typeoftable' : 'Type of Table' ,
            'mealplan' : 'Meal Plan',
            'arrivaltime' : 'Arrival Time',
            'bookdate' : 'Book Date'
        }
        widgets = { 
            'arrivaltime': forms.TimeInput(attrs={'type': 'time'}),
            'bookdate': forms.DateInput(attrs={'type': 'date'}),
            }
        exclude = ['user']
        labels= {
            'typeoftable' : 'Type of Table' ,
            'mealplan' : 'Meal Plan',
            'arrivaltime' : 'Arrival Time',
            'bookdate' : 'Book Date'
        }
         
    def adduser (self ,userId):
        self.user = userId
   

class CommentForm(forms.ModelForm):
    

    class Meta:
        model = Comment
        exclude = ['user']
        labels= {
            'title' : 'Name' ,
            'body' : 'Description' ,
        }
    def adduser (self ,userId):
        self.user = userId
        
         

    
