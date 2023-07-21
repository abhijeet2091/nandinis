from django.contrib import admin
from .models import Sweet, Order

class Sweet_Admin(admin.ModelAdmin):
    list_display=('sweet_name', 'sweet_category', 'price')
    ordering=('sweet_category', 'sweet_name')

class Order_Admin(admin.ModelAdmin):
    list_display=('order_id', 'order_dt_crt', 'order_dt_mod',
                   'sweet_name', 'order_quan', 'order_val', 'email',
                   'order_delivered', 'order_confirmed')
    ordering=('order_id',)

admin.site.register(Sweet, Sweet_Admin)
admin.site.register(Order, Order_Admin)
