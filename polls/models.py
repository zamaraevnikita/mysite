from django.db import models
from django.db import models
#Модель для обработки вопроса
class Question(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateField('date published')
    #В тотмент конвертации в str()
    def __str__(self):
        return self.text

#Модель для обработки варианта ответа на вопрос
class Choice(models.Model):
    #связываем question и choices
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)
    #В тотмент конвертации в str()
    def __str__(self):
        return self.text