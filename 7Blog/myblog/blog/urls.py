"""myblog URL Configuration
***********配置每个页面的地址***********

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')第一个参数是url，第二个是响应函数，第三个是url名称
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
#import blog.views as bv#第一种方法，但不适合多应用的网站

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name="index"),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),#没有name无法在模板中使用{%url%}
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    url(r'^edit_action$', views.edit_action,name='edit_action'),
    #url(r'^register$',views.register,name='registe'),
    #url(r'^register_action$', views.register_action,name='register_action'),
    url(r'^login$', views.login,name='login'),
    url(r'^login_action$', views.login_action,name='login_action'),
    url(r'^logout$', views.logout,name='logout'),
    url(r'^about$', views.about,name="about"),
    url(r'^articles$', views.articles,name="articles"),
    url(r'^del_article/(?P<article_id>[0-9]+)$', views.del_article,name="del_article"),
   

    #url(r'^include$', views.include,name="include"),
]#bv.index是方法名
#将article_id作为组名匹配，必须和相应函数的参数名保持一致
#Template中可以用“{% url 'app_name:url_name' param%}   ”来写url
#	 ---url作为关键字
#	 ---单引号里面的是目标地址
#	 	---其中app_name和url_name都是在项目url函数中配置的
#	 ---后面是地址参数