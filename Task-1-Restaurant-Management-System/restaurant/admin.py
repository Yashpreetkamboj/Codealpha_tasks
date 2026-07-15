from django.contrib import admin
from .models import MenuItem, Table, Inventory, Order, Reservation
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Reservation)
