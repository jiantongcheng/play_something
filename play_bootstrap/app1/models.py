# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# class OrigUser(models.Model):
#     username = models.CharField(max_length=30)
#     age = models.IntegerField()

#     def __unicode__(self):
#         return self.username

# @python_2_unicode_compatible
# class Author(models.Model):
#     name = models.CharField(max_length=20)
#     qq = models.CharField(max_length=10)
#     addr = models.TextField()
#     email = models.EmailField()
 
#     def __str__(self):
#         return self.name
 
# @python_2_unicode_compatible
# class Article(models.Model):
#     title = models.CharField(max_length=20)
#     author = models.ForeignKey(Author)
#     content = models.TextField()
#     score = models.IntegerField()  # 文章的打分
#     tags = models.ManyToManyField('Tag')
 
#     def __str__(self):
#         return self.title
 
# @python_2_unicode_compatible
# class Tag(models.Model):
#     name = models.CharField(max_length=20)
 
#     def __str__(self):
#         return self.name

class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
 
    pub_date = models.DateTimeField(u'发表时间', auto_now_add = True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.title