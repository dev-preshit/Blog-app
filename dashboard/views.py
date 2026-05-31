from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .views  import Category
from .forms import BlogForm, CategoryForm

# Create your views here.

@login_required(login_url='login_page')
def dashboard(request):

    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count' : category_count,
        'blogs_count' : blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context=context)

@login_required(login_url='login_page')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login_page')
def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context= {
        'form':form,
    }
    return render(request, 'dashboard/add_category.html',context)

def edit_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)
    context = {
        "form" : form,
        "category": category,
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login_page')
def delete_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    
    return redirect('categories')
