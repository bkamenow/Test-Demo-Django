from django.contrib import admin

from djangoTestDemo.objects_posts.models import Post, Object


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    pass
