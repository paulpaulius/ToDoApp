from django.db import models
import datetime

class List(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.CharField(max_length=200, blank=True,null=True) #models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=1), blank=True,null=True)
    def __str__(self):
        return self.name + ' | ' + str(self.completed)