from django.db import models
from django.utils import timezone
import datetime
# Create your models here
#Two models question and choice represented as classes.
class Question(models.Model):
    ques_txt=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date of Publication')
    def __str__(self):
        return self.ques_txt
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt
