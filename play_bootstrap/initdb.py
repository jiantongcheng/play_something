# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#下面三行代码从网上查到的,用于设置一些环境
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "play_bootstrap.settings")
django.setup()

import random
from django.db.models import Count
from app1.models import Author, Article, Tag

author_name_list = ['cheng', 'jian', 'tong', 'zhou', 'li']
article_title_list = ['Hello World', 'God am I', '3Q byby']

def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # print(created)
        author.qq = ''.join(str(random.choice(range(10))) for _ in range(9))
        author.addr = 'add_%s' % (random.randrange(1,3))
        author.email = '%s@jiantong.com' % author.addr
        author.save()

        # print ("---->>>>")
        # print(Author.objects.all().query)
        # print ("----")
        # print(Author.objects.values_list('name', 'addr', 'email'))
        # print ("----")
        # print(list(Author.objects.values('name', 'qq')))
        # print("----")
        # print(Author.objects.all().extra(select={'alias_name':'name'}).query)
        # print("----")
        # print(Author.objects.all().extra(select={'alias_name':'name'}).defer('name').query)
        # print("----")


def create_articles_and_tags():
    for article_title in article_title_list:
        tag_name = article_title.split(' ', 1)[0] #这里的1表示?
        tag, created = Tag.objects.get_or_create(name=tag_name)
        random_author = random.choice(Author.objects.all())

        for i in range(1, 5):
            title = '%s_%s' % (article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,
                    'content': '%s 正文' % title,
                    'score': random.randrange(70, 101),
                }
            )
            article.tags.add(tag)

def query_test():
    
    print(Article.objects.all().values('author_id').annotate(count=Count('author')).values('author_id', 'count'))

def main():
    create_authors()
    create_articles_and_tags()
    query_test()

if __name__ == '__main__':
    main()
    print("Done!")

