from typing import Any, Dict
from django.shortcuts import redirect, render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from httpcore import request

from books.forms import BookForm 
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json
from .filters import BookFilter



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('list')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

class FilterListView(ListView):
    model = Book
    template_name = 'filter.html'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter'] = BookFilter(self.request.GET, queryset = self.get_queryset())
            return context


class BooksListView(ListView):
    model = Book
    template_name = 'list.html'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter'] = BookFilter(self.request.GET, queryset = self.get_queryset())
            return context


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

# class SnippetListView(ListView):
#       model = Snippet
#       template_name = 'templates/list.html'
#       def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             context['filter'] = SnippetFilter(self.request.GET, queryset = self.get_queryset())
#             return context