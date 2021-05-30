from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from qr_survey import views

class IndexViewTestCase(TestCase):
    def test_get(self):
        req = RequestFactory().get('/qr_survey')
        req.user = AnonymousUser()
        index_view = views.index(req)

        self.assertEqual(index_view.status_code, 200)