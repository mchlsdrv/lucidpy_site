from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import FileUploadForm
from .models import File

# Create your views here.
def upload(request):
	context = {}
	if request.method =='POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		saved_name = fs.save(uploaded_file.name, uploaded_file)
		file_name = uploaded_file.name
		file_size = uploaded_file.size
		context['saved_file_url'] = fs.url(saved_name)
		messages.success(request, f'A file {file_name} was loaded successfuly!')
		messages.success(request, f'File size - {file_size} bytes')
	return render(request=request, 
				  template_name='file_converter/file_upload_form.html',
				  context=context) 


def file_list(request):
	files = File.objects.all()
	return render(request=request, 
				  template_name='file_converter/file_list.html',
				  context={'files': files})


def upload_file(request):
	if request.method == 'POST':
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('file_converter:file_list')
	else:
		form = FileUploadForm()
	return render(request=request, 
				  template_name='file_converter/file_upload.html',
				  context={'form': form})

def delete_file(request, pk):
	if request.method == 'POST':
		file = File.objects.get(pk=pk)
		file_name = file.name
		file.delete()
		messages.success(request, f'File \"{file_name}\" was deleted!')
	return redirect('file_converter:file_list')

	