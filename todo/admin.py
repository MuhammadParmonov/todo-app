from django.contrib import admin
from .models import Category, Todo
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'user']
    search_fields = ["name"]

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['datetime', 'user', 'body', 'done']
    search_fields = ['user__username']

# admin.site.register(Category, CategoryAdmin)
# admin.site.register([Todo])