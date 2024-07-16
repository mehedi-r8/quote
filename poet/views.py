from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from Quote.authentication import ApiKeyAuthentication
from .models import Poet, Category
from .serializers import PoetSerializer, CategorySerializer


class PoetDetail(generics.RetrieveAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    authentication_classes = [ApiKeyAuthentication]
class PoetList(generics.ListAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    authentication_classes = [ApiKeyAuthentication]

class CategoryListView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

