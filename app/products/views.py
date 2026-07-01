from rest_framework.decorators import  api_view, permission_classes
from rest_framework.permissions import  AllowAny

from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import *

@api_view(['GET'])
@permission_classes([AllowAny])
def product_list_api(request):
    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

