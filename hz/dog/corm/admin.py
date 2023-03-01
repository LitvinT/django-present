from django.contrib import admin

from .models import Category, Team, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'slug')
    search_fields = ('name', )
    list_filter = ('is_published', )
    ordering = ('is_published', 'name', 'slug')


@admin.register(Team)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name', )
    ordering = ('is_published', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name',)
    ordering = ('is_published', 'name', 'permission')