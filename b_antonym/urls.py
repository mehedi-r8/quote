from django.urls import path
from .views import AntonymListView

urlpatterns = [
    path('antonyms/', AntonymListView.as_view(), name='antonym-list'),
]
