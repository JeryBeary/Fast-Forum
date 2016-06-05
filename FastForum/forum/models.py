from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Thread(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200, default = "")
	pub_date = models.DateTimeField('date published')
	upvotes = models.IntegerField(default=0)
	def __str__(self):
    		return self.title

class Comment(models.Model):
	text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	upvotes = models.IntegerField(default=0)
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default="")
	#replyTo = models.ForeignKey(Comment, on_delete=models.CASCADE, default = "")
	def __str__(self):
    		return self.text 


