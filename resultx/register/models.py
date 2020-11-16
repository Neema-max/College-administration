from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    lev = models.IntegerField(default=1,choices=((1,1),(2,2),(3,3)))
    def __str__(self):
        return self.user.username
        
class subjects(models.Model):
    name = models.CharField(max_length=200,null=False)
    s_id = models.CharField(max_length=20,null=False)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    updated_at=models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return self.name
class teachers(models.Model):
    profile = models.OneToOneField(profile,on_delete = models.CASCADE)
    subject = models.ManyToManyField(subjects)
    def __str__(self):
        return self.profile.user.username

class courses(models.Model):
    name = models.CharField(max_length=200,null= False)
    c_id = models.CharField(max_length=20,null=True)
    subjects = models.ManyToManyField(subjects)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    updated_at=models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return self.name
class administrator(models.Model):
    profile = models.OneToOneField(profile,on_delete = models.CASCADE)
    def __str__(self):
        return self.profile.user.username
class student(models.Model):
    profile = models.OneToOneField(profile,on_delete = models.CASCADE)
    course = models.ForeignKey(courses,on_delete = models.CASCADE)


@receiver(post_save, sender=profile)
def profile_save(sender, instance, created , **kwargs):
    if created:
        if instance.lev == 2:
            r= teachers(profile = instance)
            r.save()
        elif instance.lev == 3: 
            r= administrator(profile = instance)
            r.save()
    else:
        if instance.lev == 1:
            instance.student.save()
        elif instance.lev == 2:
            instance.teachers.save()
        elif instance.lev == 3: 
            instance.administrator.save()