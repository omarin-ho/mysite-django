from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
