from django.db import models


# Create your models here.

class User_db (models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(default='user',max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='profile/', default='profile/def.png',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s %s" % (self.name)


class Posts(models.Model):
    title = models.CharField(max_length=300)
    
    meta = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    keywords = models.CharField(max_length=300)

    post = models.CharField(max_length=3000)

    banner_photo = models.ImageField(upload_to='post/', default='post/def.jpg',null=True,blank=True)
    body_photo = models.ImageField(upload_to='post/',null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User_db, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

