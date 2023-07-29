from django.db import models

class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField()
   owner = models.CharField(max_length=200)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',  #project variable references Project class
        on_delete=models.CASCADE, #if project is deleted, delete pledges
        related_name='pledges'  #name all the pledges related to the FK as pledges
    )
    supporter = models.CharField(max_length=200)