from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here. 


@login_required(login_url='login_page')
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


@login_required(login_url='login_page')
def category_Menu(request):
    categories = Category.objects.all()
    context = {
            'categories' : categories,
    }
    return render(request, 'category_menu.html', context)


@login_required(login_url='login_page')
def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug = slug, status = 'Published')
    if request.method == "POST":
        comment_text = request.POST.get('comment', '').strip()
        if comment_text:
            comment = Comment()
            comment.user = request.user
            comment.blog = single_blog
            comment.comments = comment_text
            comment.save()
            return redirect(reverse('blogs', args=[slug] ))
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        'slug' : slug,
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count,
    }
    return render(request,'blogs.html',context=context)


@login_required(login_url='login_page')
def search(request):
    keyword = request.GET.get('Keyword'," ")
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status = 'Published')
    context = {
        "blogs" : blogs,
        "Keyword" : keyword,
    }
    print(context)

    return render(request,'search.html',context=context)

def delete_user_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    slug = comment.blog.slug
    comment.delete()
    return redirect('blogs', slug)