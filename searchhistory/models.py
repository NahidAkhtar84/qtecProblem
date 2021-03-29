from django.db import models
import datetime
from users.models import User

# Create your models here.

class searchhistory(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    searchkey = models.CharField(max_length=255)
    searchtime = models.DateTimeField(blank=True, default=datetime.datetime.now)
    historytitle = models.CharField(max_length=1000, default='No searched title found!')
    historylink = models.CharField(max_length=1000, default='www.notfound.com')
    historysummary = models.TextField(max_length=2000)

    def __str__(self):
        return self.searchkey

