# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pub_date','update_time','title',)
    search_fields = ('title', 'content',)
    list_filter = ('title',) 

# Register your models here.
admin.site.register(Article, ArticleAdmin)
