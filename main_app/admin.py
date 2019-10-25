from django.contrib import admin
from .models import Post, Topic, SubTopic
from tinymce.widgets import TinyMCE
from django.db import models


class PostAdmin(admin.ModelAdmin):
	# fields = ['topic',
	# 		  'title',
	# 		  'date',
	# 		  'content']
	fieldsets = [
				('Basic Information', {'fields': ['title', 'date']}),
				('sub topic', {'fields': ['sub_topic']}),
				('URL', {'fields': ['slug']}),
				('Post Content', {'fields': ['content']}),
				]
	formfield_overrides = {
							models.TextField: {'widget': TinyMCE()}
						  }

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Post, PostAdmin)
