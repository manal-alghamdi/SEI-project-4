
# ItalianHouse

> An application that provides a service for booking a table in your favorite restaurant, you can also view the reservations that have been booked and edit, cancel them.

## Description
The user will be able to view the menu and book a table with specfic date and time. the user must fell all the froms including his/her name, email, contact number and number of guest. The resturant will send a booking confirmation to the email. Finally the user can edit and delete the booking when plan has changed.


## Why (ItalianHouse) ?

> You do not have to wait in line in order to eat in this restaurant 

> “Always On” Service and Improved service.

> Saving Time, Money, & Paper


## User stories

> As an admin, I can add, edit, and delete the useres and reservations, I also can edit the restaurant menu.

> As a user, I can book a tables that are avalible to me.

> As a user, I can sign up and login to book a table.

> As a user, I can login to see my profile and update it.

> As a user, I can choose the date and time when I want to book an appointment.

> As a user, I can view all his reservations and cancel & edit them.

> as a user I want to be able to view the menu 



### Use-Case digram
![User Story](https://i.imgur.com/JOmkDpa.png)




### Platforms

Platform| Status
------------ | -------------
Microsoft Windows | ✓
Linux  | ✓
Mac os | ✓
Android  | ✓

#### Built With 
- [Visual Studio](https://visualstudio.microsoft.com/)
- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Postgresql](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [CSS, HTML]


## App Wireframes

Home         |  Login | SignUp       |  EditReservation      |  Menu     |  Add comment
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------|:-------------------------:|:-------------------------:
<img src="https://i.ibb.co/qg6SNdy/Screenshot-2021-02-17-114403.png" title="Home App  Login " width="100%"> |<img src="https://i.ibb.co/tZfj1LK/Screenshot-2021-02-17-114428.png" title="SignUp" width="100%">|<img src="https://i.ibb.co/7yh29Hh/Screenshot-2021-02-17-114454.png" title="Login" width="100%"> |<img src="https://i.ibb.co/3YPKH3J/Screenshot-2021-02-17-114552.png" title="Login" width="100%"> |<img src="https://i.ibb.co/QfH9j3r/Screenshot-2021-02-17-114515.png" title="Clinics" width="100%">|<img src="https://i.ibb.co/2hKxrVG/Screenshot-2021-02-17-114611.png" title="Clinics" width="100%">

## Folder Structure
    .
    ├── register
    ├── restaurant                       
    ├── restaurantApp                     
    ├── staticfiles                           
    ├── .DS_Store
    ├── manage.py
    ├── menu.json
    ├── pipfile
    ├── pipfile.lock
    ├── procfile.js
    ├── requirments.txt
    └── README.md


#### Clone Project

```shell
git clone https://git.generalassemb.ly/Fire-sparks/Steakhouse.git
```
![https://git.generalassemb.ly/Fire-sparks/Steakhouse.git]

This Command  will copy a full  project  to your local  environment

## How to Setup

### Setting up The Backend

```shell
    cd Steakhouse
    pipenv shell
    pipenv install
    python manage.py runserver
```



## REST  API


### App API

APP API| URL 
------------ | ------------- 
admin | /admin
Signup |register 
Login | accounts/login/
Logout |accounts/logout/  
Home | home/
Menu |menu/ 
About Us | /aboutUs/ 
Profile/ |/editProfile/ 
Reservation/ | /myReservation/



## Website Link 
> ################################

## Future work

> Enable user to switch from english to arabic languge.

> Add other type of restaurant.

> Enable the customr to choose a restaurant.

## Planning and Development Process

First we came up with the idea, creating user stories, then we created the wireframe to get the full pictuer of the website and to create the database schema. lastly we are going to start coding the application.


### Problem-Solving Strategy
- Searching in the internet for problem solutions and try to figure out the way to solve it
- Look for similar project in the internet to see how they were solving the same matter
- Ask for help from other teams 
- Ask the instructors for help

### Unsolved problems
- We tried to import google map in our about page to show the exact address of our store but failed to due to acceptance of google. They asked us a certificate of the place ownership

### Acknowledgment
- we would like every one who helped us see this project come to live: 
- Marco Santonastasi
- Yasir Al-Muhtrish
- Ali Hamidaddin 
- Haneen Alghamdi  
- Sara-kuddah 


This was a wonderful journey "Thank you All"







