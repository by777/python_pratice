from django.db import models#数据模块，使用ORM框架
from django.contrib.auth.models import AbstractUser
#通常，一个Model对应数据库的一张数据表
#Django中Models以类的形式表现
#它包含了一些基本字段以及数据的一些行为
#ORM：对象关系映射（Object Relation Mapping）实现了对象和数据库之间的映射，隐藏了数据访问的细节
#创建类，继承models.Model，该类即是一张数据表
#在类中创建字段
#字段创建，字段即类里面的属性（变量）
#attr = model.CharField(max_length=64)
#Doc：http://docs.djangoproject.com/en/1.10/ref/models/fields/
#

# Create your models here.
class  Article(models.Model):
	title = models.CharField(max_length=64,default="Title")
	content = models.TextField(null=True,default="Content")
	pub_time = models.DateTimeField(null=True,auto_now=True)#null=True使其可以修改 auto_now=True自动创建时间
	tag = models.CharField(max_length=32,default="未分类")
	#comments = models.TextField(null=False,default=" ")
	ordering = ['-pub_time']
	def __str__(self):#__str__()方法是当这个类的实例被打印的时候应该显现什么的方法，self实例自己的title属性
		return self.title
#class Meta:  #按时间下降排序
#        ordering = ['-date_time']
#创建完成后执行pyhton manage.py makemigrations app名（数据迁移）
#然后再执行python manage.py migrate执行数据迁移动作
#程序会在app/migrations/目录下生成迁移文件
#
#
#
#但是在创建完成后使用Admin管理后，会显示对象的默认名称Artcle Object
#需要修改数据的默认显示的名称
#	---在Article类下添加一个方法
#	---Python3使用__str__(self)、python2.7使用__unicode_(self)
#	---return self.title
class User_Account(models.Model):
	user_name = models.CharField(max_length=32,null=False)
	user_pwd = models.TextField(max_length=160)
	user_email = models.CharField(max_length=32,null=True)
	
	login_time = models.DateTimeField(null=True,auto_now=True)
	def __str__(self):
		return self.user_name


# class User(AbstractUser):
#     # 手机号
#     user_phone = models.CharField(blank=True, verbose_name='电话', max_length=11)
#     #判断是否是认证通过的用户
#     user_isValid=models.BooleanField(blank=True,default=False)

#     def __str__(self):
#         return self.username
class Article_Comments(models.Model):
	article_id = models.ForeignKey(Article,related_name='article_id')
	visitor_name = models.CharField('visitor_name',max_length=40)
	comment_time = models.DateField('comment_time')
	comments = models.TextField('comments',max_length=200)
	
	
	

'''
一、一对多（外键）
例子：一个作者对应多本书，一本书只有一个作者
model代码：
[python] view plain copy
class Person(models.Model);  
name = models.CharField('作者姓名', max_length=10)  
age = models.IntegerField('作者年龄')  
  
class Book(models.Model):  
person = models.ForeignKey(Person, related_name='person_book')  
title = models.CharField('书籍名称', max_length=10)  
pubtime = models.DateField('出版时间')  

（一）获取对象方法：
1.从作者出发获取书籍
[python] view plain copy
person = Person.objects.fiter(你的条件)  
book = person.book_set.all()  

2.从书籍出发获取作者
[python] view plain copy
p = book.person  

二、多对多
例子：一个作者对应多本书，一本书有多个作者
model代码：
[python] view plain copy
class Author(models.Model):    
    first_name = models.CharField(max_length=30)    
    last_name = models.CharField(max_length=40)    
    email = models.EmailField()    
        
class Book(models.Model):    
    title = models.CharField(max_length=200)    
    authors = models.ManyToManyField(Author)    

（一）获取对象方法：
1.从书籍出发获取作者
[python] view plain copy
b = Book.objects.get(id=50)  
b.authors.all()  
b.authors.filter(first_name='Adam')  
2.从作者出发获取书籍


[python] view plain copy
a = Author.objects.get(id=1)  
a.book_set.all()  
（二）添加对象方法：
[python] view plain copy
a = Author.objects.get(id=1)  
b = Book.objects.get(id=50)  
b.authors.add(a)  


（三）删除对象对象方法：
[python] view plain copy
a = Author.objects.get(id=1)  
b = Book.objects.get(id=50)  
b.authors.remove(a) 或者 b.authors.filter(id=1).delete() 
 '''