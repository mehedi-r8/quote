from rest_framework import generics

from Quote.authentication import ApiKeyAuthentication
from .models import Poet
from .serializers import PoetSerializer

class PoetDetail(generics.RetrieveAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    authentication_classes = [ApiKeyAuthentication]
class PoetList(generics.ListAPIView):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer
    authentication_classes = [ApiKeyAuthentication]