from rest_framework import viewsets

from Quote.authentication import ApiKeyAuthentication
from .models import Writer, Quote
from .serializers import WriterSerializer, QuoteSerializer


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    # authentication_classes = [ApiKeyAuthentication]
    # permission_classes = [IsAuthenticated]


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    authentication_classes = [ApiKeyAuthentication]
