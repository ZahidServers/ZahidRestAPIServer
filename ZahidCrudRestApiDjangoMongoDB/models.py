from django.db import models
class movie(models.Model):
	name = models.TextField(max_length=255, blank=False, default='')
	img = models.TextField(max_length=255, blank=False, default='')
	summary = models.TextField(max_length=255,blank=False, default='')