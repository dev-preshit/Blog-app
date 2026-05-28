from .models import Category,Blog,About,SocialLinks


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_About(request):
    try:
        contact = About.objects.get()
    except About.DoesNotExist:
        contact = None
    return dict(contact = contact)

def get_SocialLinks(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links = social_links)