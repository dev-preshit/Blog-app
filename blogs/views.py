from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
def post_by_category(request, category_id):

    category_name = get_object_or_404(Category,id = category_id).category_name
    featured_post = Blog.objects.filter(is_featured = True,status="Published", category =category_id).order_by("-created_at")
    simple_post = Blog.objects.filter(is_featured = False,status="Published", category =category_id).order_by("-created_at")
    categories = Category.objects.all()
    context = {
            'Name_of_perticular_category' : category_name,
            'categories' : categories,
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