from django.db import models

# Create your models here.
class Post(models.Model):
	doc=models.FileField()
	caption=models.CharField(max_length=100)
	
	
	def __str__(self):
		return self.caption	