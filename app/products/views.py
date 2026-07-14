from rest_framework.decorators import  api_view, permission_classes
from rest_framework.permissions import  AllowAny
from rest_framework import generics
from django_filters import rest_framework as filters

from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import *

@api_view(['GET'])
@permission_classes([AllowAny])
def product_list_api(request) -> Response:
    products = Product.objects.values('id', 'product_name', 'stock', 'price')

    serializer = ListModelSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def product_info(request, pk) -> Response:
    product_data = Product.objects.filter(pk=pk)
 
    if not product_data.exists():
        return Response(
            {"error": "Specified id is not avaiable in Database."}, 
            status=status.HTTP_404_NOT_FOUND
        )
 
    serialize = ProductSerializer(product_data, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)

class ProductFilterList(generics.ListAPIView):
    queryset = Product.objects.filter(status='Active')
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['product_name' ,'category', 'price', 'sold_count']
    permission_classes = [AllowAny]


