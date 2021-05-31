from django.test import TestCase
from qr_survey.models import Poster, Question, Answer

class PosterTestCase(TestCase):
    def setUp(self):
        self.poster = Poster(name='Test Poster', qr_id='qr12344')

    def test_poster_str(self):
        self.assertEquals(str(self.poster), 'Test Poster qr12344')
    
    def test_get_poster_name(self):
        self.assertEquals(self.poster.get_poster_name(), 'Test Poster')
    
    def test_get_qr_id(self):
        self.assertEquals(self.poster.get_qr_id(), 'qr12344')

class QuestionTestCase(TestCase):
    def setUp(self):
        self.question = Question(text='What are you?')

    def test_question_str(self):
        self.assertEqual(str(self.question), 'What are you?')

class AnswerTestCase(TestCase):
    def setUp(self):
        self.question = Question(text='What are you?')
        self.answer = Answer(question=self.question, answer=3)

    def test_answer_str(self):
        self.assertEquals(str(self.answer), '3')
    
    def test_question_text(self):
        self.assertEquals(str(self.answer.get_question()), 'What are you?')

    def test_answer_value(self):
        self.assertEquals(self.answer.get_answer(), 3)
