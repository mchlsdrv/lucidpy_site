from django.db import models
from datetime import datetime


# Create your models here.
class Topic(models.Model):
	name = models.CharField(max_length=100)
	summary = models.CharField(max_length=500)
	slug = models.CharField(max_length=200, default=1)

	class Meta:
		# Gives a proper plural name
		verbose_name_plural = 'Topics'

	def __str__(self):
		return self.name


class SubTopic(models.Model):
	topic = models.ForeignKey(Topic, default=1, verbose_name='Topic', on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=100)
	summary = models.CharField(max_length=500)

	class Meta:
		verbose_name_plural = 'SubTopics'

	def __str__(self):
		return self.name


class Post(models.Model):
	sub_topic = models.ForeignKey(SubTopic, default=1, verbose_name='SubTopic', on_delete=models.SET_DEFAULT)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField('publishing date', default=datetime.now())
	slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = 'Posts'
		
	def __str__(self):
		return self.title

