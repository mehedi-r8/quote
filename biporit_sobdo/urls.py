from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OppositeWordViewSet

router = DefaultRouter()
router.register(r'oppositewords', OppositeWordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
