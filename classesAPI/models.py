from django.db import models

# Create your models here.
class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	# teacher = models.ForeignKey(User, on_delete=models.CASCADE)