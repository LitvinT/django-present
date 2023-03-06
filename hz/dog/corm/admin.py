from django.contrib import admin

from .models import Category, Team, Comment, Contact, Product, Text, Gallery, Descr, Right, BlockQ, Left, Countries


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'descr')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'category')


@admin.register(Right)
class RightAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'descr', 'image')


@admin.register(Left)
class RightAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'descr', 'image')


@admin.register(Descr)
class DescrAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'category', 'descr')


@admin.register(BlockQ)
class BlockqAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'descr')


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'number', 'image', 'perc', 'visits', 'color')
