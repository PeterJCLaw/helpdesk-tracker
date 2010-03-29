from django.db import models

# Create your models here.

OPEN_STATUS = 1
IN_PROGRESS_STATUS = 2
CLOSED_STATUS = 4
WONT_FIX_STATUS = 8
CANT_REPRODUCE_STATUS = 16

class issue (models.Model):
	team = models.CharField(max_length=1000)
	shortDesc = models.CharField(max_length=100)
	assignedTo = models.CharField(max_length=40)
	initialDesc = models.TextField()
	ongoingNotes = models.TextField()
	status = models.IntegerField()
	updated = models.DateTimeField(auto_now=True)
