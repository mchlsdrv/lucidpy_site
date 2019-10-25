from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist 
from .models import Topic, SubTopic, Post
from .forms import CustomUserCreationForm


# Create your views here.
def single_slug(request, slug):
	print(f'slug = {slug}')
	topic_slug_list = [topic.slug for topic in Topic.objects.all()]
	if slug in topic_slug_list:
		matching_sub_topics = SubTopic.objects.filter(topic__slug=slug)
		sub_topics_urls_dict = {}
		for matching_sub_topic in matching_sub_topics.all():
			try:
				fst_post = Post.objects.filter(sub_topic__name=matching_sub_topic.name).earliest('date')
				sub_topics_urls_dict[matching_sub_topic] = fst_post.slug
			except ObjectDoesNotExist  as error_message:
				print(f'Error in sub_topics : {error_message}')
			except AttributeError  as error_message:
				print(f'Error in sub_topics : {error_message}')
		return render(request=request, 
					  template_name='main_app/sub_topics.html', 
					  context={'sub_topics_urls_dict': sub_topics_urls_dict})

	post_slug_list = [post.slug for post in Post.objects.all()]
	if slug in post_slug_list:
		current_post = Post.objects.get(slug=slug)
		posts_from_sub_topic = Post.objects.filter(sub_topic__name=current_post.sub_topic).order_by('date')
		current_post_index = list(posts_from_sub_topic).index(current_post)
		return render(request=request, 
					  template_name='main_app/post.html',
					  context={'current_post': current_post, 
					  		   'current_post_index': current_post_index, 
					  		   'sidebar_data': posts_from_sub_topic
					  		  }
					 )

	return HttpResponse(f'{slug} does not correspond to anything we know of!')

def home(request):
	# return HttpResponse('Lucid <strong>PY</strong>thon')
	return render(request=request, template_name='main_app/topics.html', context={'topics': Topic.objects.all})


def register_request(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'A new account {username} has been created!')
			login(request, user)
			return redirect('main_app:home')
		else:
			for msg in form.error_messages:
				print(f'{msg}: {form.error_messages[msg]}')
				messages.error(request, f'{msg}: {form.error_messages[msg]}')
			return render(request=request, template_name='main_app/register.html', context={'form': form})
	form = CustomUserCreationForm
	return render(request=request, template_name='main_app/register.html', context={'form': form})


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				messages.success(request, f'U r logged in successfully as {username}!')
				login(request, user)
				return redirect('main_app:home')
			else:
				messages.error(request, '#Invalid username or password!')
		else:
			messages.error(request, '!Invalid username or password!')
	form = AuthenticationForm()
	return render(request=request, template_name='main_app/login.html', context={'form': form})


def logout_request(request):
	# form = AuthenticationForm()
	# username = form.username
	logout(request)

	messages.info(request, f'Logged out successfully!')

	return redirect('main_app:home')
