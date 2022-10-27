from django.contrib import admin
from blog.models import Comment, Resp, Site
from user.models import Profile
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query = super(PostAdmin, self).get_queryset(request)
        filtered_query = Comment.objects.none()
        profile = Profile.objects.get(user=request.user)
        site = Site.objects.filter(user=profile)
        for s in site:
            filtered_query |= query.filter(site=s)
            print(s.title)
        return filtered_query
    search_fields = ('body',)
    list_filter = ('slug', 'status', 'created', 'publish', 'author',)
    #prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_display = ('site', 'body', 'slug', 'created', 'publish', 'author')


class RespAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query = super(RespAdmin, self).get_queryset(request)
        filtered_query = Resp.objects.none()
        profile = Profile.objects.get(user=request.user)
        site = Site.objects.filter(user=profile)
        for s in site:
            filtered_query |= query.filter(site=s)
        return filtered_query
    search_fields = ('commento', 'body')
    list_display = ('id', 'site', 'commento', 'body', 'created',
                    'publish', 'author', 'respToUser', 'idRespTo', 'postType')
    list_filter = ('created', 'commento', 'publish', 'author')
    date_hierarchy = 'publish'
    ordering = ('commento', 'publish')


class classSite(admin.ModelAdmin):
    def get_queryset(self, request):
        query = super(classSite, self).get_queryset(request)
        filtered_query = Site.objects.none()
        profile = Profile.objects.get(user=request.user)
        site = Site.objects.filter(user=profile)
        for s in site:
            filtered_query |= query.filter(user=profile)
            print(s.title)
        return filtered_query
    list_filter = ('title', 'user', 'titleTagContent')
    list_display = ('title', 'user', 'titleTagContent')
    search_fields = ('user',)


class classProfile(admin.ModelAdmin):
    def get_queryset(self, request):
        query = super(classProfile, self).get_queryset(request)
        filtered_query = Profile.objects.none()
        profile = Profile.objects.get(user=request.user)
        filtered_query |= query.filter(user=profile.user)
        return query
    list_filter = ('user',)


admin.site.register(Site, classSite)
admin.site.register(Resp, RespAdmin)
admin.site.register(Comment, PostAdmin)
admin.site.register(Profile, classProfile)
