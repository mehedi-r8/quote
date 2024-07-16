from django.urls import path
from .views import PoetDetail, PoetList, CategoryListView

urlpatterns = [
    path('poets/', PoetList.as_view(), name='poet-list'),
    path('poet/<int:pk>/', PoetDetail.as_view(), name='poet-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
