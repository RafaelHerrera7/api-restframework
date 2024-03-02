from django.db import models

# Create your models here.
#VAR

#TOPIC
class Topic(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

#TEACHER
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
      
    def __str__(self):
        return self.name

#COURSE
class Course(models.Model):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title


    


    
    

    
