import datetime
import uuid

from django.db import models
from django.utils import timezone
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text

class ExampleModel(Model):
  _DATABASE = "cass_db"
  id = columns.BigInt(primary_key=True)
  created_at = columns.DateTime()
  deleted = columns.Boolean(default=False)