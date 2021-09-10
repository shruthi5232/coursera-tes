from django.shortcuts import render
from .forms import ImageForm
import os
from blog import imagetopattern as imtp
from django.core.files.storage import FileSystemStorage

def getpathmain(files):#path of files from main directory
	settings_dir = os.path.dirname(__file__)
	PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
	path = os.path.join(PROJECT_ROOT, files)
	return path
def getpathcwd(files):#path of files in current working directory
	return os.path.join(os.path.dirname(os.path.realpath(__file__)), files)
filepath=getpathcwd('words.txt')
# Create your views here.


def home(request):
	#context={'data':data}
	return render(request,'blog/index.html')
	return render(request,'blog/home.html')
	return render(request,'blog/contact.html')
def imagetopattern(request):

	if request.method == 'POST':
		imageform = ImageForm(request.POST, request.FILES)
		context={'title':'home','imageform':imageform,'lct':'40','uct':'200','resolution':'10','yourimage':'your image'}
		lcolour=request.POST.get('lct')
		context['lct']=lcolour
		ucolour=request.POST.get('uct')
		context['uct']=ucolour
		#print('clr',lcolour,ucolour)
		if request.POST.get('button') == 'pressed':
			imgpath=getpathmain(r'media\images')
			files = [f for f in os.listdir(imgpath)]
			os.chdir(imgpath)
			for i in files:
				if not i == "heart.png":
					os.remove(i)
			return render(request,'blog/home.html',context)
		
		elif imageform.is_valid():
			imgfunction=context['imageform'].cleaned_data['imgfunction']
			character=context['imageform'].cleaned_data['name']
			if character=="":
				character='-'
			resolution=request.POST.get('resolution')
			imageform.save()
			# Get the current instance object to display in the template
			img_obj = imageform.instance
			imgpath=getpathcwd(img_obj.image.url)
			if imgpath[len(imgpath)-9:]=='heart.png':
				context['yourimage']='default image - http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js'
			imtp.imgtoptn(imgpath,filepath,imgfunction,resolution,c=character,l=lcolour,u=ucolour)
			with open(filepath,'r',encoding='utf-8') as w:
				#debugcontext={'post':imageform.cleaned_data}
				newcontext={'mytext':w.read(), 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js':http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js ,'lines':w.readlines()}
				context.update(newcontext)
				return render(request, 'blog/index.html',context )
	else:
		imageform = ImageForm()
		context={'title':'contact','imageform':imageform}
		return render(request,'blog/contact.html',context)

