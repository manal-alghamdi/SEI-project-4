from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/<str:category>', views.filter_menu, name='category'),
    path('bookTable/', views.bookTable, name='bookTable'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('myReservation/', views.myReservation, name='myReservation'),
    path('cancel_reservation/<int:pk>/delete', views.cancel_reservation, name='cancel_reservation'), 
    path('edit_reservation/<int:pk>/edit', views.edit_reservation, name='edit_reservation'),
    
    path('addcomment/', views.addcomment, name='addcomment'),
    
    
]