from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'Delivery_Charge', 'status', 'pincode', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

# class PaymentAdmin(admin.ModelAdmin):
#         list_display = ['user', 'order_number', 'Payment_captured', 'full_name', 'Phone_number', 'Swamy_order_number', 'status']
#         list_filter = ['status', 'Payment_captured']
#         search_fields = ['order_number', 'Phone_number']
#         list_per_page = 20




admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
