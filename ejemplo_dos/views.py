from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from ejemplo_dos.models import Post 
from django.urls import reverse_lazy
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "ejemplo_dos/index.html", {} )

    
class PostDetalle(DetailView):
    model = Post

class PostListar(ListView): #Login required mixin SIEMPRE va primero
    model = Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'


class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

class UserSignup(CreateView):
    form_class = UsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("ejemplo-dos-listar")

class UserLogin(LoginView):
    next_page = reverse_lazy("ejemplo-dos-listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("ejemplo-dos-listar")
