from django.db import models

# Create your models here.
class student(models.Model):
    
    name=models.TextField(max_length=20)
    age=models.IntegerField()

    def _str_(self):
        return self.name +"_"+str(self.age)


class Game(models.Model):
       name=models.CharField(max_length=30)
       description=models.TextField(max_length=100)
       
       def _str_(self):
           return self.name +"_"+self.description