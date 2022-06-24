from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class PostListView(ListView):
    model=Post 
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostCreateView(CreateView):
    model=Post 
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostDetailView(DetailView):
    model=Post 

class PostUpdateView(DetailView):
    model=Post 
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model=Post 
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
