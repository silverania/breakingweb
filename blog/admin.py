from django.contrib import admin
from blog.models import Comment, Resp, Site
from user.models import Profile
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ('body',)
    list_filter = ('slug', 'status', 'created', 'publish', 'author',)
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_display = ('slug', 'created', 'publish', 'author')


class RespAdmin(admin.ModelAdmin):
    search_fields = ('commento', 'body')
    list_display = ('id', 'commento', 'body', 'created',
                    'publish', 'author', 'respToUser', 'idRespTo', 'postType')
    list_filter = ('created', 'commento', 'publish', 'author')
    date_hierarchy = 'publish'
    ordering = ('commento', 'publish')


class classSite(admin.ModelAdmin):
    list_filter = ('title',)


class classProfile(admin.ModelAdmin):
    list_filter = ('user',)


admin.site.register(Site, classSite)
admin.site.register(Resp, RespAdmin)
admin.site.register(Comment, PostAdmin)
admin.site.register(Profile, classProfile)
