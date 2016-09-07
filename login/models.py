from django.db import models

# Create your models here.

class Participant(models.Model):
	participant_name = models.CharField(max_length=30)
	college_name = models.CharField(max_length=100)
	score = models.IntegerField(default=0)

	def __str__(self):
		return (self.participant_name + ", " + self.college_name + ", " + str(self.score))