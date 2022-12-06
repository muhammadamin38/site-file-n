from django.contrib import admin
from .models import Post
from .models import TopPost


# admin.site.register(Post)
# admin.site.register(TopPost)

@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('ism',)
    list_display = ('ism','malumot','tanlov')


    