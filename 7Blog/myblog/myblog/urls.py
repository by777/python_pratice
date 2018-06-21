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
from django.conf.urls import url,include 
from django.contrib import admin
#import blog.views as bv#第一种方法，但不适合多应用的网站
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.jump),
    url(r'^blog/', include('blog.urls',namespace='blog')),#这一个index指的总路径
   # url(r'^blog2/', include('blog2.urls')),
]#bv.index是方法名
