from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic =models.TextField()
    desc=models.TextField()
    def __str__(self):
        return self.topic
    

class Question(models.Model):
    topic= models.ForeignKey(Topic, related_name='Topic', on_delete=models.CASCADE)
    question=models.TextField()
    difficulty= models.IntegerField()
    point=models.IntegerField() 
    def __str__(self) -> str:
        return self.question             
    
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    review=models.ManyToManyField(Question,related_name="review")
    completed=models.ManyToManyField(Question,related_name="completed")
    def __str__(self) -> str:
        return self.user.username
        