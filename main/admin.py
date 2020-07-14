from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # #changes order in admin
    # fields = ["tutorial_title",
    #         'tutorial_published',
    #         'tutorial_content',
    #         ]

    # creating sets to segment
    fieldsets = [
        ("Title/Date", {"fields": ['article_title', 'article_published']}),
        ("Image", {"fields": ['article_image']}),
        ("Content", {'fields': ['article_slug', 'article_content']})
    ]

    # add MCE only to our tutorial fields
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Article, ArticleAdmin)