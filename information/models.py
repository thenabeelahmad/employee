from django.db import models

# Create your models here.
class Information(models.Model):
	Iname=models.CharField(max_length=100)
	Imob=models.IntegerField(max_length=10)
	Imail=models.EmailField()
	Iadhar=models.IntegerField()
	Isalary=models.IntegerField()

	def __str__(self):
		return self.Iname