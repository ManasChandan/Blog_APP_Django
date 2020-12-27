from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.edit import UpdateView , DeleteView
from . predictions import Classifier
from . ThirdAPI import Weather
# Create your views here.



# def home(request):
#     context = {
#         'posts' : Post.objects.all() , 'title' : 'Home' , 
#     }
#     return render(request , 'blog/home.html' , context=context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    weather = Weather()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["weather"] = self.weather.CityWeather()
        if 'city' in self.kwargs:
            context["weather"] = self.weather.CityWeather(self.kwargs['city'])
        else:
            context["weather"] = self.weather.CityWeather()
        return context

class PostDetailView(DetailView):
    model = Post
    classifier = Classifier()
    weather = Weather()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = super().get_object()
        context["number"] = self.classifier.classify(str(data.content))
        return context
    


class CreatePostView(LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePostView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request , 'blog/about.html' , {'title' : 'about'})