from django.db import models
from django.contrib.auth.models import User



class UserPage(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='newlist',null=True )
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name} {self.user} {self.user.id}"

class Link(models.Model):
    user = models.ForeignKey(UserPage,on_delete=models.CASCADE,null=True)
    links = models.CharField(max_length=200)
    linkname = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.links} {self.linkname} {self.user} {self.user.id}"