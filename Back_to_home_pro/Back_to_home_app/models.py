from django.db import models

# Create your models here.
class userclass(models.Model):
    image = models.ImageField(upload_to='user_images/')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    phonenumber2 = models.IntegerField()
    code = models.IntegerField()
    def __str__(self):
        return self.name
class admin_table(models.Model):
    user_name = models.CharField(max_length=90)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name