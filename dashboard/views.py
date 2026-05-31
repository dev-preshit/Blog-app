from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .views  import Category
from .forms import BlogForm, CategoryForm
from django.template.defaultfilters import slugify

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


@login_required(login_url='login_page')
def blogs(request):
    return render(request, "dashboard/blogs.html")

@login_required(login_url='login_page')
def add_blogs(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.slug = slugify(form.cleaned_data['title']) + "-" + str(post.id)
            post.save()
            return redirect('blogs')
        else:
            print(form.errors)
    else:
        form = BlogForm()
    context={
        "form" : form,
    }
    return render(request, "dashboard/add_blogs.html",context=context)

@login_required(login_url='login_page')
def edit_blogs(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)  
            post.slug = slugify(form.cleaned_data['title']) + "-" + str(post.id)
            post.save()
            return redirect('blogs')
        else:
            print(form.errors)
    else:
        form = BlogForm(instance=blog)
    context={
        "form" : form,
        "blog" : blog
    }
    return render(request, "dashboard/edit_blogs.html",context=context)

@login_required(login_url='login_page')
def delete_blogs(request,pk):
    category = get_object_or_404(Blog, pk=pk)
    category.delete()
    
    return redirect('blogs')