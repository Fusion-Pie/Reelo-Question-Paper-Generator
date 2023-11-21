from django.db import models

# Create your models here.
class QuestionsDB(models.Model):
    questionId = models.AutoField(primary_key = True)
    question = models.CharField(max_length = 500)
    category = models.CharField(max_length = 200)
    correctAns = models.CharField(max_length = 100)
    incorrectAns = models.CharField(max_length = 500)
    
    DIFFICULTY_CHOICES = [
        ('NA', 'None'),
        ("easy", "easy"),
        ("medium", "medium"),
        ('hard', 'hard')
    ]

    difficulty = models.CharField(choices = DIFFICULTY_CHOICES, default = 'NA', max_length = 10)

    TYPE_CHOICES = [
        ('None', 'None'),
        ('multiple', 'multiple'),
        ('boolean', 'boolean')
    ]

    type = models.CharField(choices = TYPE_CHOICES, default = 'None', max_length = 10)