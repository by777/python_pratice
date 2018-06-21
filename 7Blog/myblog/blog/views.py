from django.shortcuts import render#执行响应的逻辑代码，大部分代码在这里编写
from django.http import HttpResponse
from . import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist#判断记录是否存在
from django.http import HttpResponseRedirect
from django.utils.timezone import now, timedelta
import time
boo_login = 'False'
#from django.template.context_processors import csrf
#from django.contrib.auth import logout as auth_logout

#logout：该函数接受一个HttpRequest对象，无返回值。
	#当调用该函数时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错
# Create your views here.
#def index(request):#必须接收一个请求，一般约定为request
#	#return HttpResponse('Hello World!')#每个响应对应一个函数，函数必须返回一个响应
#	return render(request,"blog/index.html")#request请求对象本身，index函数




		# rander()函数中支持一个dict类型参数
		# 该字典是后台传递到模板的参数，键为参数名
		# 在模板中使用{{参数名}}来直接使用


	#取出数据库内容
	#import models
	#article = models.Article.objects.get(pk=1)(primay_key=1比较方便)
	#render(request,page,{'article':article})传（对象）到前端
def index(request):
	#article = models.Article.objects.get(pk=1)#object实例对象
	articles = models.Article.objects.all()#获取所有的文章列表
	try:
		boo_login = str(request.session['boo_login'])
	except:
		boo_login = 'False'
	finally:
		
		return render(request,"blog/index.html",{'articles':articles[::-1],'boo_login':boo_login})

def article_page(request,article_id):
	boo_login = 'False'
	article = models.Article.objects.get(pk=article_id)
	try:
		boo_login = str(request.session['boo_login'])
	except:
		boo_login = 'False'
	finally:
		return render(request,"blog/article_page_new.html",{'article':article,'boo_login':boo_login})

def edit_page(request,article_id):
	boo_login = 'False'
	tags_raw = []
	#articles = models.Article.objects.all()
	tags = models.Article.objects.all()
	for tag in tags:
		tags_raw.append(tag.tag)

	#for obj in objs:
		#tags_raw.append(objs.tag)
	#for tags in tags_raw:
	tags_new = {}.fromkeys(tags_raw).keys()
	
	try:
		boo_login = request.session['boo_login']
	except:
		boo_login = 'False'	
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	if  str(boo_login) !='True':
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	#return HttpResponseRedirect(article_id)
	else:

		if str(article_id) =='0':#判断新建
			
			return render(request,"blog/edit_page_new.html",{'tags_new':tags_new,'boo_login':boo_login})
		else:
			article = models.Article.objects.get(pk=article_id)
			#return render(request,'blog/edit_page.html')
			return render(request,'blog/edit_page_new.html',{'article':article,'tags_new':tags_new,'boo_login':boo_login})


def edit_action(request):#获取request中的数据
	try:#为了防止利用URL攻击，此处也要进行验证登陆状态
		boo_login = request.session['boo_login']
	except:
			
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	if  str(boo_login) !='True':
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	else:
		title = request.POST.get('title','TITLE')
		content = request.POST.get('content','CONTENT')
		article_id=request.POST.get('article_id','0')
		
		tag2 = request.POST.get('tag2','TAG')
		
		tag1 = request.POST.get('tag1','TAG')
		if len(tag2) == 0:
			tag = tag1
		else:
			tag =tag2

		#boo_login = request.session['boo_login']
		

		if article_id =='0':

			models.Article.objects.create(title=title,content=content,tag=tag)#创建新表栏
			articles = models.Article.objects.all()
			return render(request,"blog/index.html",{'articles':articles})#创建新文章的动作，返回主页
		else:
			article=models.Article.objects.get(pk=article_id)
			#修改原数据
			article.title = title
			article.content = content
			article.tag = tag
			article.save()
			return render(request,"blog/article_page_new.html",{'article':article})

#前端步骤
#模板可直接使用对象以及对象的“.”操作
# ---eg：{{article.title}}
'''
def register(request):
	return render(request,"blog/register_page.html")

为多用户做准备的，未完成
def register_action(request):
	user_name = request.POST.get('user_name','USER_NAME')
	user_pwd = request.POST.get('user_pwd','USER_PWD')
	user_pwd = make_password(user_pwd)#进行加密处理
	try:
		
		user_account_exist = models.User_Account.objects.filter(user_name=user_name)#判断是否用户已存在
		if not user_account_exist:#user_account_exist实际返回一个对象，也可以使用len(user_account_exist)>0来判断

			models.User_Account.objects.create(user_name=user_name,user_pwd=user_pwd)#创建新表栏
			return render(request,'blog/login_success.html')
		else:
			return render(request,'blog/login_fail.html')
	except ObjectDoesNotExist:
		#return render(request,'blog/login_success.html')
		return render(request,'blog/login_fail.html')	
'''


def login(request):
	global referer
	request.session['login_from'] = request.META.get('HTTP_REFERER', '/blog')
	try:
		boo_login = str(request.session['boo_login'])
	except:
		boo_login = 'False'
		
	if boo_login == 'True':
		return render(request,'blog/login_page.html',{'user_name':'恁已登陆，不需要重复登陆'})
	if request.method=='POST':

		return HttpResponseRedirect(referer)
	else:
		try:
			referer = request.META['HTTP_REFERER']  # 获取网页访问来源
		except:
			pass
		finally:
			return render(request,'blog/login_page.html')



def login_action(request):
	
	
	#if request.method == 'GET':
		#request.session['login_from'] = request.META.get('HTTP_REFERER', '/')

	
	user_name = request.POST.get('user_name','USER_NAME')
	user_pwd = request.POST.get('user_pwd','USER_PWD')#表单传来的
	try:
		user_pwd_admin = models.User_Account.objects.get(user_name=user_name).user_pwd#数据库中正确的#######
	#user_pwd = make_password(user_pwd)#加密，但是加密应该是注册时候的
	except:
		return render(request,'blog/login_page.html',{'login_error':'用户名错误','user_name':user_name})
	login_result = check_password(user_pwd,user_pwd_admin)
	if login_result:
		#user_name = authenticate(username=user_name,password=user_pwd)#认证
		#auth_login(request,user_name)
		now_time =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		user=models.User_Account.objects.get(user_name=user_name)
		user.login_time=now_time
		user.save()
	       #return HttpResponseRedirect(referer)
		request.session['boo_login']='True'
		#request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
		#return HttpResponseRedirect('/blog')	
		return HttpResponseRedirect(request.session['login_from'])
		#这里我们使用的是：request.META[‘HTTP_REFERER’]
		#大概实现的思路是：在login函数内声明一个全局变量referer，
		#在不是发生post请求的时候记录下来源页面赋值给referer，在是发生post请求后返回到原页面。代码如下：
	else:
		return render(request,'blog/login_page.html',{'login_error':'密码错误','user_name':user_name})
		#return HttpResponseRedirect(request.session['login_from'])	
	
def logout(request):
	try:
		del request.session['boo_login']
	except :
		pass
	#return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/blog'))#重定向到了首页
	return HttpResponse("You're logged out")
# def all(request):
#     if request.user.is_authenticated:
#         user_name=request.user_name
#     else:
#         user_name=''
#     return render(request, 'news.html', {
#         'user_name': user_name,
#     })
    #在其登录之后会将用户信息保存在request中，那么我们我进行一个views 函数前，
    #可以先判断下request.user是否存在，如存在将数据传递给返回前端，如果不存在我们也可以添加一些其他的逻辑。	
def about(request):
	#user = models.User_Account.objects.get(user_name=)
	articles = models.Article.objects.all()#获取所有的文章列表
	
	#return render(request,"blog/index.html",{'articles':articles})
	return render(request,'blog/other.html',{'articles':articles})
def articles(request):

	articles = models.Article.objects.all()
	try:
		boo_login = str(request.session['boo_login'])
	except:
		boo_login = 'False'
	finally:
		return render(request,'blog/articles_view.html',{'articles':articles,'boo_login':boo_login})	

def del_article(request,article_id):
	try:
		boo_login = request.session['boo_login']
	except:
		boo_login = 'False'	
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	if  str(boo_login) !='True':
		#return HttpResponse("还没有登陆")
		return HttpResponseRedirect('/blog/login')
	#return HttpResponseRedirect(article_id)
	else:
		del_article = models.Article.objects.get(pk=article_id)
		del_article.delete()

	return HttpResponseRedirect('/blog/')
def jump(request):
	return HttpResponseRedirect('/blog/')
# def comments(request):
# 	#Article_Comments = models.Article.objects.fiter(pk=1)
# 	return HttpResponse("Yoo")
	