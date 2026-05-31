from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),

    
    path('categories/', views.categories, name="categories"),
    path('categories/add', views.add_categories, name="add_categories"),
    path('categories/edit/<int:pk>/', views.edit_categories, name="edit_categories"),
    path('categories/delete/<int:pk>/', views.delete_categories, name="delete_categories"),
    
    
    path('blogs/', views.blogs, name="blogs"),
    path('blogs/add', views.add_blogs, name="add_blogs"),
    path('blogs/edit/<int:pk>/', views.edit_blogs, name="edit_blogs"),
    path('blogs/delete/<int:pk>/', views.delete_blogs, name="delete_blogs"),

    path('users/',views.users, name='users'),
    path('users/add', views.add_users, name="add_users"),
    path('users/edit/<int:pk>/', views.edit_users, name="edit_users"),
    path('users/delete/<int:pk>/', views.delete_users, name="delete_users"),
]
