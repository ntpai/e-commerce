from django.urls import path
import products.views as views
from products.serializers import ProductSerializer
from products.models import Product


urlpatterns = [
    path("list/", views.product_list_api, name="products_list"),
    path("id/<int:pk>/", views.product_info, name="product_info"),
    path("search/", views.ProductFilterList.as_view(), name="product_filter"),
]