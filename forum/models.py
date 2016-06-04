from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

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


