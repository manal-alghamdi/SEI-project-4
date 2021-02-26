from django.http import request
from django.shortcuts import render,redirect , HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm
from django.contrib import messages
from .forms import EditUserProfileForm , ReservationForm , CommentForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.utils.timezone import utc
# Create your views here.
def index(request):
    allComments=Comment.objects.all()
    return render(request,'restaurant/home.html' , {"allComments" : allComments})


def home(request):
    allComments=Comment.objects.all()
    return render(request,'restaurant/home.html' , {"allComments" : allComments})

def addcomment(request):
    user=User.objects.get(pk=request.user.id)
    form = CommentForm()
    if request.method == "POST":
            comment = CommentForm(request.POST)
            if comment.is_valid():
                comment1 =comment.save(commit = False)
                comment1.user=user
                comment1.save()
                return redirect('/home') 
    else:
        return render(request,'restaurant/addcomment.html' ,{ 'form':form})

# show all meals
def menu(request):
    menu_item = Menu.objects.all()
    return render(request,'restaurant/menu.html', {'menu_item':menu_item} )

def filter_menu(request, category):
    filter_meals = Menu.objects.filter(category = category)
    return render(request,'restaurant/menu.html', {'menu_item':filter_meals} )
    
def aboutUs(request):
    return render(request,'restaurant/aboutUs.html')


@login_required
def bookTable(request):
    user=User.objects.get(pk=request.user.id)
    form = ReservationForm()
    if request.method == "POST":
        book = ReservationForm(request.POST)
        if book.is_valid():
            #------------Time
            time1 = request.POST.get('arrivaltime')
            time2 = str(datetime.datetime.now().time().strftime("%H:%M"))
            time11 = datetime.datetime.strptime(time1 ,"%H:%M")
            time22 = datetime.datetime.strptime(time2 ,"%H:%M")
            # ------------Date
            date1 = request.POST.get('bookdate')
            date2 = str(datetime.date.today())
            date11 = datetime.datetime.strptime(date1 ,"%Y-%m-%d")
            date22 = datetime.datetime.strptime(date2 ,"%Y-%m-%d")
            print("tiimmee11: " , time1)
            print("tiimmee22: " , time2)
            if date11 < date22:
                messages.success(request , 'Please choose valid date')
                return redirect('/bookTable')
            elif time11 < time22 and date11 > date22:
                book1 =book.save(commit = False)
                book1.user=user
                book1.save()
                return redirect('/myReservation') 
            elif time11 < time22 : 
                messages.success(request , 'Please choose valid time')
                return redirect('/bookTable')
            elif time11 == time22 and date11 == date22: 
                messages.success(request , 'Please choose valid time')
                return redirect('/bookTable')
            elif time11 > time22 and date11 == date22:
                book1 =book.save(commit = False)
                book1.user=user
                book1.save()
                return redirect('/myReservation')
            elif time11 == time22 and date11 > date22:
                book1 =book.save(commit = False)
                book1.user=user
                book1.save()
                return redirect('/myReservation')
            elif time11 > time22 and date11 > date22:
                book1 =book.save(commit = False)
                book1.user=user
                book1.save()
                return redirect('/myReservation')
            else:
                book1 =book.save(commit = False)
                book1.user=user
                book1.save()
                return redirect('/myReservation')   
    else:
        return render(request,'restaurant/bookTable.html' , {'form' : form})

@login_required
def editProfile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserProfileForm(request.POST ,instance=request.user)
            messages.success(request , 'Profile Updated')
            form.save()
            return redirect('/editProfile')
        else:
            form = EditUserProfileForm(instance=request.user)
            return render(request,'restaurant/editProfile.html' , {'name': request.user , 'form':form})
    else:
        return redirect('/editProfile')
        
@login_required
def changePassword(request):
    if request.method == "POST":
      form = PasswordChangeForm(user=request.user , data=request.POST) 
      if form.is_valid():
          form.save()
          update_session_auth_hash(request, form.user)
          return redirect("/home")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'restaurant/changePassword.html' ,{'name': request.user , 'form':form})


@login_required
def myReservation(request):
    user=User.objects.get(pk=request.user.id)
    data=user.Reservations.all()
    return render(request,'restaurant/myReservation.html' , {"data" : data})

def cancel_reservation(requset , pk ):
    reservation=Reservations.objects.get(id=pk)
    reservation.delete()
    return redirect('myReservation')

def edit_reservation(request,pk):
    if (request.method == "POST"): 
        reservation=Reservations.objects.get(pk=pk)
        form = ReservationForm(request.POST , instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('/myReservation')          
    else:
        reservation=Reservations.objects.get(pk=pk)
        form = ReservationForm(instance=reservation)
    return render(request , 'restaurant/edit_reservation.html' , {"form" : form})


