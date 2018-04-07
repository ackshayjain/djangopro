from django.db import models

# Create your models here.

class Test(models.Model):

	title = models.CharField(max_length=200)
	pic = models.ImageField(upload_to='img',default='')



	def __unicode__(self):
		return self.title
