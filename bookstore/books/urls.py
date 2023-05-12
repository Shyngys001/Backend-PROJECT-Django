
from django import views
from . import views
from django.urls import path
from .views import BooksListView, BooksDetailView, BookCheckoutView, FilterListView, add_book, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('filters', FilterListView.as_view(), name = 'filter'),
    path('add_book/', add_book, name='add_book'),
]