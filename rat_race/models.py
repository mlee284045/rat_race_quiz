from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Runner(User):
    location_lat = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    location_long = models.DecimalField(max_digits=6, decimal_places=2, null=True)



class Topic(models.Model):
    # think about a way to reset finished field whenever people start a new quiz but
    question = models.TextField()
    answer = models.CharField(max_length=60)
    finished = models.BooleanField(default=False)


    # Trying to create a self-assigning difficulty function that can give a tag of
    # Difficult or Easy based on how many times it was answered correctly. Not sure
    # if it belongs here though. Need to figure how to calculate percentage correct.
    #
    # def assign_difficulty(self):
    #     if self.finished and


class Quiz(models.Model):
    name = models.CharField(max_length=60)
    topics = models.ForeignKey(Topic, related_name='quiz')
    runners = models.ForeignKey(Runner, related_name='quiz')