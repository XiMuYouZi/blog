from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.models import Article
admin.site.register(Article)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<mky>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^$', 'article.views.home'),

)
