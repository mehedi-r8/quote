from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WriterViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r'writers', WriterViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
