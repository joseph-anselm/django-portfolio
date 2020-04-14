from django.shortcuts import render
from .models import blog

# Create your views here.
def home(request):
    blog = blog.objects.all()
    return render(request, 'blog/home.html', {'blog':blog})