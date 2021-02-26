from django.contrib import admin
from .models import Reservations, Menu , Comment
# Register your models here.

# admin.site.unregister(User)
admin.site.register(Reservations)
admin.site.register(Menu)
admin.site.register(Comment)