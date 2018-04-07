from django.db import models

# Create your models here.

class Test(models.Model):

	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title
