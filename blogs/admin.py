from django.contrib import admin
from .models import Category, Blog, About, SocialLinks

# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status', 'is_featured' )
    list_editable = ('status','is_featured')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


class aboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        
        if count == 0:
            return True
        return False


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,aboutAdmin)
admin.site.register(SocialLinks)