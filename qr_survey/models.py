from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Poster(models.Model):
    name = models.CharField(max_length=30, verbose_name='poster name', unique=True)
    qr_id = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.name} {self.qr_id}'
class Question(models.Model):
    text = models.TextField(max_length=100, verbose_name='questions text')

    def __str__(self):
        return f'{self.text}'
class Answer(models.Model):
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        related_name='answer_to_question'
    )
    value = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
     )
    
    def __str__(self):
        return f'{self.value}'
