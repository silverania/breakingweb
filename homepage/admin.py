from django.contrib import admin
from .models import Tutorial, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'visite', 'slug', 'status')
    search_fields = ('title', 'slug', 'status')


class CategoryData(admin.ModelAdmin):
    search_fields = ('title', 'created', 'updated')
    list_display = ('title', 'created', 'updated')


admin.site.register(Tutorial, PostAdmin)
admin.site.register(Category, CategoryData)
