from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = [
        "name_facebook",
        "href_value",
        "ptit",
        "birth_of_date",
        "department",
        "orientation",
        "main_programming_language",
        # "priority",
        "other_note",
    ]
    

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"



class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")