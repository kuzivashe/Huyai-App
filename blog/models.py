from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	'''the difference between reverse and redirect is that reverse returns the url as a string and lets
	the urls.py redirect it, while redirect will send us to a specific url'''
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
