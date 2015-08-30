# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404,HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包

def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 2) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})

def about_me(request) :
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__contains = tag) #contains
        print tag
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list1 = Article.objects.filter(content__icontains=s)
            post_list2=Article.objects.filter(title__contains=s)
            post1=[]
            post2=[]
            post=[]

            for posts in post_list1:
                post1.append(posts)
            for postss in post_list2:
                    post2.append(postss)

            print 'post1:'+post1
            print 'post2:'+post2

            for i in post1:
               if not i in post2:
                      post2.append(i)
            print 'hebing post2:'+post2

            if len(post2)== 0 :
                return render(request,'archives.html', {'post_list' : post2,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post2,
                                                    'error' : False})
    return  HttpResponseRedirect('/')