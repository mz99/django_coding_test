from django.db import models

class Question(models.Model):
    question_text  = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    yes_no = models.BooleanField(default=True)
