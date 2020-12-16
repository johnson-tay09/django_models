from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "post-detail.html"
    model = Post
