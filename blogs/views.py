from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.
def post_by_category(request, category_id):

    category_name = get_object_or_404(Category,id = category_id).category_name
    featured_post = Blog.objects.filter(is_featured = True,status="Published", category =category_id).order_by("-created_at")
    simple_post = Blog.objects.filter(is_featured = False,status="Published", category =category_id).order_by("-created_at")
    context = {
            'Name_of_perticular_category' : category_name,
            'featured_post' : featured_post,
            'simple_post' : simple_post,
               }
    return render(request, 'category.html', context)

def category_Menu(request):
    categories = Category.objects.all()
    context = {
            'categories' : categories,
    }
    return render(request, 'category_menu.html', context)

def blogs(request,slug):

    single_blog = get_object_or_404(Blog, slug = slug, status = 'Published')

    context = {
        'slug' : slug,
        'single_blog' : single_blog,
    }
    return render(request,'blogs.html',context=context)

def search(request):
    keyword = request.GET.get('Keyword'," ")
    blogs = Blog.objects.filter(Q(title__icontains=keyword) |Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword),status = 'Published')
    context = {
        "blogs" : blogs,
        "Keyword" : keyword
    }
    print(context)

    return render(request,'search.html',context=context)