##summer
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from django.contrib import admin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Post, PostAdmin)
