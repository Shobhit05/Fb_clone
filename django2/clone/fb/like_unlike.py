from django.shortcuts import render,redirect

from . models import LikePost,Post,Connection




def like(request,id):
	obj1=LikePost.objects.filter(person=request.user,post_id=id)
	obj=Post.objects.get(id=id)
	like=LikePost.objects.filter(person=request.user)
	if not len(obj1) == 1:
		C=LikePost(post_id=id,person=request.user)
		C.save()
		obj.like=obj.like+1
	 	obj.save()
	 	return redirect("index")



def likefromdetail(request,id):
	obj1=LikePost.objects.filter(person=request.user,post_id=id)
	obj=Post.objects.get(id=id)
	like=LikePost.objects.filter(person=request.user)
	if not len(obj1) == 1:
		C=LikePost(post_id=id,person=request.user)
		C.save()
		obj.like=obj.like+1
	 	obj.save()
	 	return redirect("detail",id)



def unlike(request,id):
	obj1=LikePost.objects.filter(person=request.user,post_id=id)
	obj=Post.objects.get(id=id)
	q=Connection.objects.all().filter(user=request.user)
	if obj1:
		obj1.delete()
		obj.like=obj.like-1
	 	obj.save()
	 	return redirect("index")

def unlikefromdetail(request,id):
	obj1=LikePost.objects.filter(person=request.user,post_id=id)
	obj=Post.objects.get(id=id)
	q=Connection.objects.all().filter(user=request.user)
	if obj1:
		obj1.delete()
		obj.like=obj.like-1
	 	obj.save()
	 	return redirect("detail",id)