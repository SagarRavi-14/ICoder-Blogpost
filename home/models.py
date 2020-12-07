from django.db import models

# Create your models here.
class Contact(models.Model):
    srn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=20,default="")
    query = models.CharField(max_length=500,default="")
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

