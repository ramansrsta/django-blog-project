from django.shortcuts import render
from .models import Blog

# Create your views here.
def index_page_view(request):
    return render(request,'index.html')


def blog_view(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html',{'blog':blog})