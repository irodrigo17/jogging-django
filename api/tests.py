from django.test import TestCase
from api.models import Jog
from django.contrib.auth.models import User
import datetime

class JogTests(TestCase):

    def test_str(self):
        user = User.objects.create(username='jdoe', email='jdoe@email.com')
        date = datetime.datetime.now()
        jog = Jog.objects.create(user=user, date=date, meters=1230.3, seconds=3671.1)
        expected_result = '{user}, {date}'.format(user=str(user), date=str(date))
        self.assertEqual(str(jog), expected_result)

    def test_avg_speed(self):
        user = User.objects.create(username='jdoe', email='jdoe@email.com')
        date = datetime.datetime.now()
        jog = Jog.objects.create(user=user, date=date, meters=2800, seconds=700)
        self.assertEqual(jog.average_speed(), 4.0)
