from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-data_posted']
    paginate_by = 5
