from django.urls import path
from django.conf.urls import url
from .views import ItemListView,ItemListCatoIdView,ItemListSellerView,ItemListNameView

urlpatterns = [
    path('all', ItemListView.as_view()), #all item product url
    url(r"^category/(?P<category_id>\d+)/?$", ItemListCatoIdView.as_view(), name="category"), #listing a category's items url ex. /category/1
    url(r"^seller/(?P<seller>[\w\-]+)/$", ItemListSellerView.as_view(), name="seller"),#listing a seller's items url ex. /seller/<companyx>
    url(r"^name/(?P<itemname>[\w\-]+)/$", ItemListNameView.as_view(), name="itemname"),#listing an item using name url ex. /name/<itemname>
]
