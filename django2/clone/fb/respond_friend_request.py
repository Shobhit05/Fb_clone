from django.shortcuts import render,redirect

from . models import Connection,Addrequest



def addfriend(request,friend):
	if not Connection.objects.filter(user=request.user,friend=friend):
		if not Addrequest.objects.filter(person=request.user,requests=friend ):
			if not Addrequest.objects.filter(person=friend,requests=request.user):
				C=Addrequest(person=request.user,requests=friend)
				C.save()
	
	return redirect("index")

def accept(request,addfriend):
	if not Connection.objects.filter(user=request.user,friend=addfriend):
		
		C=Connection(user=request.user,friend=addfriend)
		C.save()
		D=Connection(user=addfriend,friend=request.user)
		D.save()
		d=Addrequest.objects.filter(person=addfriend,requests=request.user)
		d.delete()
	
	return redirect("index")






def unfriend(request,name):
	obj1=Connection.objects.filter(user=request.user,friend=name)
	obj2=Connection.objects.filter(user=name,friend=request.user)
	obj1.delete()
	obj2.delete()

	return redirect("index")

def cancelrequest(request,name):
	obj1=Addrequest.objects.filter(person=name,requests=request.user)
	if obj1:

		obj1.delete()
	else:
		obj1=Addrequest.objects.filter(person=request.user,requests=name)
		obj1.delete()

	return redirect("index")