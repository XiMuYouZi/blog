from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.models import Article
admin.site.register(Article)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'article.views.about_me', name = 'about_me'),
    url(r'^tag(?P<tag>.*)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','article.views.blog_search', name = 'search'),



)
