from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70)
    content = models.TextField(max_length=5000)
    slug = models.CharField(max_length=250)
    time_stamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return (self.title + ' by ' + self.author)