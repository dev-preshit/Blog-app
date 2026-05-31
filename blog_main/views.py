from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog


def home(request):
    featured_post = Blog.objects.filter(is_featured = True,status="Published").order_by("-created_at")
    simple_post = Blog.objects.filter(is_featured = False,status="Published").order_by("-created_at")
    context = {
               'featured_post' : featured_post,
               'simple_post':simple_post,}
    return render(request, 'home.html',context=context)