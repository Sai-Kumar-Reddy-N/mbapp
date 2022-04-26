from django.db import models

class Posts(models.Model):
    Name = models.CharField(max_length=20,blank=True)
    Mobile_No =  models.CharField(max_length = 20,blank=True)
    State = models.CharField(max_length=30,blank=True)
    
    