from django.contrib import admin
from products.models import Product

@admin.action(description="Change status of the selected product(s) to Inactive.")
def to_inactive(modeladmin, request, queryset):
    queryset.update(status="Inactive")

@admin.action(description="Change status of the selected product(s) to Active.")
def to_active(modeladmin, request, queryset):
    queryset.update(status="Active")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'stock', 'price']
    actions = [to_active, to_inactive]
