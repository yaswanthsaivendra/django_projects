from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('username', 'user@gmail.com','password1!')
        self.assertIsInstance(user,User)

    def test_creates_superuser(self):
        user=User.objects.create_superuser('username', 'user@gmail.com','password1!')
        self.assertIsInstance(user,User)

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='',email='user@gmail.com',password='password1!')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='username',email='',password='password1!')

    def test_creates_superuser_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='username', email='user@gmail.com', password='password1!', is_staff=False)

    def test_creates_superuser_with_is_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='username', email='user@gmail.com', password='password1!', is_superuser=False)