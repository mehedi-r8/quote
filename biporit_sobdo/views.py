from rest_framework import viewsets, pagination

from Quote.authentication import ApiKeyAuthentication
from .models import OppositeWord
from .serializers import OppositeWordSerializer

class OppositeWordPagination(pagination.PageNumberPagination):
    page_size = 30  # 30 items per group

class OppositeWordViewSet(viewsets.ModelViewSet):
    queryset = OppositeWord.objects.all()
    serializer_class = OppositeWordSerializer
    pagination_class = OppositeWordPagination
    authentication_classes = [ApiKeyAuthentication]
