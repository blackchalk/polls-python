import datetime
from django.db import models
from django.utils import timezone

#testing again here some wakatime error: resolving with 
#deleting the .wakatime.cfg file and restoring vscode and entering the api key
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #changing the default header and value of fields
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

#model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text