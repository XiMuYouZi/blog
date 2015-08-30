from django.test import TestCase
from article.models import Article
# Create your tests here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.conf import settings
settings.configure()

post_list1 = Article.objects.filter(content__icontains='django')
post_list2=Article.objects.filter(title__contains='django')
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