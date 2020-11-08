from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView

# Create your tests here.
class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Signup')
        self.assertNotContains(self.response, 'hi there!, i should not be on this page')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup')
        self.assertEqual(view.func.__name__,
        SignupPageView.as_view().__name__)


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username="will",
        email='will@email',
        password='willpass'
        )

        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
        username = "admin",
        email = 'admin@email',
        password = 'adminpass'
        )

        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@email')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)