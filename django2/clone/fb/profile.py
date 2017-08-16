from django.shortcuts import render

from . models import Person

from .forms import ProfileForm,CoverimageForm

def myprofile(request):
	query=Person.objects.filter(username=request.user)
	profilepic=Person.objects.filter(username=request.user)
	
	form=ProfileForm(request.POST or None,request.FILES or None)
	form2=CoverimageForm(request.POST or None,request.FILES or None)
	if form2.is_valid():
		if bool(form2.cleaned_data["coverpic"]) == True:
			pic=Person.objects.get(username=request.user)
			pic.coverpic=form2.cleaned_data["coverpic"]
			pic.save()
	if form.is_valid():
		if bool(form.cleaned_data["profilepic"]) == True:
			pic=Person.objects.get(username=request.user)
			pic.profilepic=form.cleaned_data["profilepic"]
			pic.save()
	context={
	"query":query,
	"form":form,
	"profilepic":profilepic,
	"form2":form2,
	
	}
	return render(request,"profile.html",context)





	


def profile1(request,pk):
	query=Person.objects.filter(id=pk)
	name=query[0]
	context={
	"query":query,
	"name":name,
	}
	return render(request,"profile1.html",context)
