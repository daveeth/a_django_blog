from django.shortcuts import render
from django.views.generic import (
	TemplateView, ListView, DetailView, 
	CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post


# Create your views here.

class HomePV(ListView):
	model = Post
	template_name = 'home.html' 

class BlogDetailV(DetailView):
	model = Post
	template_name = 'detail.html'

class BlogCreateV(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'body']

class BlogUpdateV(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']

class BlogDeleteV(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
		
