from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Poster(models.Model):
    name = models.CharField(max_length=30, verbose_name='poster name', unique=True)
    qr_id = models.CharField(max_length=20, blank=True)

    def get_poster_name(self):
        return self.name

    def get_qr_id(self):
        return self.qr_id

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
        related_name='answer_to'
    )

    answer = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
     )
    
    def get_question(self):
        return self.question
    
    def get_answer(self):
        return self.answer

    def __str__(self):
        return f'{self.answer}'
