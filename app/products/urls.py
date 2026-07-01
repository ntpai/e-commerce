from django.urls import path
import products.views as views

urlpatterns = [
    path("list/", views.product_list_api, name="products_list"),
]