from django.urls import path
from .views import AddItemView, UpdateItemView

urlpatterns = [
    path('add', AddItemView.as_view()),         # adding an item url; /add
    path('update',UpdateItemView.as_view()),    # update an item url; /update
]
