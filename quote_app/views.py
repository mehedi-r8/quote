from rest_framework import viewsets

from .authentication import ApiKeyAuthentication
from .models import Writer, Quote
from .serializers import WriterSerializer, QuoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    # authentication_classes = [ApiKeyAuthentication]
    # permission_classes = [IsAuthenticated]


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    authentication_classes = [ApiKeyAuthentication]
