from django.contrib import admin
from blog.models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at', 'update_at']
    list_filter = ['create_at', 'update_at']
    search_field = ['title', 'content']

admin.site.register(BlogPost, BlogPostAdmin)
