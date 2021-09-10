from django import forms
from .models import Image
from django.utils.safestring import mark_safe




img_function=((0,'simple uniform'),(1,'multiple uniform'),(2,'multiple random'))
class ImageForm(forms.Form,forms.ModelForm):
	name = forms.CharField(label='Character', max_length=10,required=False,initial='-',widget=forms.TextInput(
attrs={'size':'2', 'class':'inputText'}))
	imgfunction= forms.ChoiceField(label="Choose a function",choices=img_function, widget=forms.RadioSelect())

	class Meta:
		model = Image
		fields = ('image','name','imgfunction')

