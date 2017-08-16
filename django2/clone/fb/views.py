from django.shortcuts import render,redirect

from django.views.generic.list import ListView

from django.http import HttpResponse,Http404
from datetime import time
from .forms import PostForm,Update,ProfileForm,CommentForm,CoverimageForm
from . models import Person,Post,LikePost,Addrequest,Connection,CommentPost,LoginDetail
from operator import itemgetter,attrgetter
from itertools import chain


#--------------------------------Handling The 404 Error Page -------------------------------------------#	


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)



def index(request):
	form=PostForm(request.POST or None,request.FILES or None)


#--------------------------------SAVING THE DATABASE USING AJAX -------------------------------------------#	
	# if request.is_ajax():
	# 	post=request.POST.get("post")
	# 	image=request.FILES.get("image")
	# 	print image
		
	# 	if bool(post) == True or bool(image) == True:
	# 		c=Post(person=request.user,post=post,image=image)
	# 		c.save() 


#---------------------------------SAVING THE DATABASE NORMALLY ------------------------------------------#

	if request.user.is_authenticated():

		if form.is_valid():
			if bool(form.cleaned_data["post"])==True or bool(form.cleaned_data["image"])==True:
				c=Post(person=request.user,person_id=request.user.id,
					post=form.cleaned_data["post"],
					image=form.cleaned_data["image"])
				c.save()
				return redirect("index")
		query1=[]
		postsort=[]
		liking={}




		name=Person.objects.filter(username=request.user)
		if not name:
			form1=Update(request.POST or None)
			if form1.is_valid():
				c=Person(username=request.user,
					First_name=form1.cleaned_data["First_name"],
					Last_name=form1.cleaned_data["Last_name"],
					sex=form1.cleaned_data["sex"],
					birthdate=form1.cleaned_data["birthdate"])

				c.save()
				return redirect("index")
			context={"form1":form1
			}
			return render(request,"update_detail.html",context)
		q=Connection.objects.all().filter(user=request.user)
		for i in q:
			
			postsort=chain(postsort,(Post.objects.filter(person=i)))
		 	
		postsort=chain(postsort,(Post.objects.filter(person=request.user)))
		postsort=sorted(postsort,key=attrgetter('timestamp'))
		for i in postsort:
			q=bool(LikePost.objects.filter(post_id=i.id,person=request.user))
			if q ==True:
				liking[i.id]=1
			else:
				liking[i.id]=0

		
		for m in range(1,len(postsort)+1):
			query1.append(postsort[-m])
		total=Connection.objects.filter(user=request.user)
		total=len(total)
		postlikedperson={}

		for i in postsort:
			q=LikePost.objects.filter(post_id=i.id)
			postlikedperson[i.id]=[j.person for j in q]



#---------------------------------------GETTING THE PROFILEPIC URL QUERY----------------------------------#
		

		profileimgurl=[]
		persons=[]
		for i in postsort:
			x=Person.objects.filter(username=i.person)
			for i in x:
				persons.append(i.username)
		persons=list(set(persons))
		for i in persons:
			x=Person.objects.filter(username=i)
			for i in x:
				if i.profilepic:
					profileimgurl.append([str(i),i.profilepic.url])

       

		profilepic=Person.objects.filter(username=request.user)
		query2=Person.objects.filter(username=request.user)
		requests=Addrequest.objects.filter(requests=request.user)
		like=LikePost.objects.filter(person=request.user)
		friendlist=Connection.objects.filter(user=request.user)
		addfriend=Person.objects.exclude(username=request.user)
		pendingrequest1=Addrequest.objects.filter(person=request.user)
		requestorder=Addrequest.objects.filter(requests=request.user)
		
		p=[]
		for i in pendingrequest1:
			p.append(i)
		pendingrequest=Person.objects.filter(username__in=p)

		t=[]
		p=[]
		for i in  friendlist:
			t.append(i.friend)
			p.append(i.friend)
		for i in pendingrequest:
			t.append(i)
		
		for i in requestorder:
			t.append(i.person)
		t.append(request.user)

		b=Person.objects.exclude(username__in=t)
		c=Person.objects.filter(username__in=p)

		logindetail=LoginDetail.objects.filter(person=request.user)
		address=request.META.get("HTTP_X_FORWARDE_FOR")
		if not address:
			address=request.META.get("REMOTE_ADDR")
		if logindetail:
			for i in logindetail:
				if str(i) != str(address):
					save=LoginDetail(person=request.user,ipaddress=address)
					save.save()
		else:
			save=LoginDetail(person=request.user,ipaddress=address)
			save.save()



    #  <!---------------------------------------THE PERSON WHO LIKES THE PHOTOS ---------------------------> #			

		postid=[]
		dic={}
		data=[]

		for i in postsort:
			postid.append(i.id)
		postid=list(set(postid))

		for i in postid:
			dic[i]=[]

		for i in postid:
			a=LikePost.objects.filter(post_id=i)
			for j in a:
				x=Person.objects.filter(username=j.person)
				for k in x:
					data.append([k.id,k.username])
				dic[i]=data
			data=[]


		
		context={"form":form,
		"query1":query1,
		"query2":query2,
		"requests":requests,
		"addfriend":addfriend,
		"like":like,
		"total":total,
		"liking":liking,
		"friendlist":friendlist,
		"b":b,
		"c":c,
		"pendingrequest":pendingrequest,
		"profilepic":profilepic,
		"postlikedperson":postlikedperson,
		"dic":dic,
		"profileimgurl":profileimgurl,



		}



		return render(request,"home.html",context)
	else:
		return redirect("auth_login")




def detail(request,id):
	commentform=CommentForm(request.POST or None)
	obj=Post.objects.get(id=id)
	if commentform.is_valid():
		a=CommentPost(person=request.user,person_id=request.user.id,post_id=id,comment=commentform.cleaned_data["comment"])
		a.save()
		obj.comment=obj.comment+1
		obj.save()
		return redirect("detail" ,id)

	# <!---------------------------       COLLECTING COMMENTS --------------------------> # 

	comments=CommentPost.objects.filter(post_id=id) 


	
	
	like=LikePost.objects.filter(person=request.user)
	q=Connection.objects.all().filter(user=request.user)
	liking={}
	postsort=[]
	for i in q:
		postsort=chain(postsort,(Post.objects.filter(person=i)))
		 	
		postsort=chain(postsort,(Post.objects.filter(person=request.user)))
		postsort=sorted(postsort,key=attrgetter('timestamp'))
		for i in postsort:
			q=bool(LikePost.objects.filter(post_id=i.id,person=request.user))
			if q ==True:
				liking[i.id]=1
			else:
				liking[i.id]=0

	context={
	"obj":obj,
	"like":like,
	"liking":liking,
	"commentform":commentform,
	"comments":comments,
	}
	
	return render(request,"detail.html",context)









# def edit_favorites(request):
#     if request.is_ajax():
#         message = "Yes, AJAX!"
#     else:
#         message = "Not Ajax"
#     return HttpResponse(message)


# # class index(ListView):

# 	template_name="home.html"
# 	model=Person
	


	
# 	def get_context_data(self,*args,**kwargs):
# 		context=super(index,self).get_context_data(*args,**kwargs)

	
		
# 		self.user=self.request.user
# 		name=Person.objects.filter(profile_name=self.user)
# 		if  not name:
# 			c=Person(profile_name=self.user)
# 			c.save()
		
# 		post=Post.objects.filter(person=self.user)
# 		context["post"]=post
		

# 		return context