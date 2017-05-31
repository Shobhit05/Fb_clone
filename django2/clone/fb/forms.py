
from django import forms

from . models import Person,Post

from django.forms.extras.widgets import SelectDateWidget


class PostForm(forms.Form):
	post = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':60,'style':'resize:none'}),required=False)
	image=forms.ImageField(required=False)

class Update(forms.ModelForm):
	birthdate=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
	class Meta:
		model=Person
		fields=["First_name","Last_name","sex","birthdate"]


class ProfileForm(forms.ModelForm):
	profilepic=forms.ImageField(required=False)
	class Meta:
		model=Person
		fields=["profilepic"]


class CommentForm(forms.Form):
	comment=forms.CharField(widget=forms.Textarea(attrs={'rows':1,'cols':22,'style':'resize:none'}),required=False)


class CoverimageForm(forms.Form):
	coverpic=forms.ImageField(required=False)
	class Meta:
		model=Person
		fields=["coverpic"]
