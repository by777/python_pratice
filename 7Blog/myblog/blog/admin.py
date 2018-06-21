from django.contrib import admin
#当前应用下的后台管理系统的配置文件，每一个应用下都有
#Admin是Django自带的一个功能强大的自动化数据管理界面
#被授权的用户可以直接在Admin中管理数据库
#Django提供了许多针对Admin的定制功能
#使用pyhton manage.py createsuperuser 创建超级用户
#在这里引入自身的models模块或模型类，否则admin只能管理admin自己的用户和组
#添加：admin.site.register(models.Article)
# Register your models here.

from . import models
#from models import Article不知为何，此处无法引入models模块，所以上面指定了.文件路径，也许试试from blog.Template import models
Article = models.Article
User_Account = models.User_Account
Article_Comments = models.Article_Comments
#admin.site.register(models.Article)
#此时再去Admin可以管理站点的数据库文件
#
#创建admin配置类继承
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','pub_time','tag')#增加属性，显示其他字段
	list_filter = ('pub_time',)	
								 #过滤器，元组只有一个元素时记得加逗号
class User_Account_Admin(admin.ModelAdmin):
	list_display = ('user_name','user_pwd')
class Article_Comments_Admin(admin.ModelAdmin):
	list_display = ('article_id','comments','visitor_name',)


	
admin.site.register(Article,ArticleAdmin)
admin.site.register(User_Account,User_Account_Admin)
admin.site.register(Article_Comments,Article_Comments_Admin)



