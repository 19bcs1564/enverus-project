from django.db import models



    # Create your models here.
class Questions(models.Model):
    QuestionId = models.AutoField(primary_key=True)
    Title= models.CharField(max_length = 200)
    OptionA = models.CharField(max_length = 200)
    OptionB = models.CharField(max_length = 200)
    OptionC = models.CharField(max_length = 200)
    OptionD = models.CharField(max_length = 200)
    Answer = models.CharField(max_length = 1)
