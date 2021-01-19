from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        user1 = get_user_model()

        user = user1.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='test',
            phone_number='000000000000'
        )

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@gmail.com')

        self.assertTrue(user.password)
        self.assertTrue(user.phone_number)

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        super_user1 = get_user_model()

        admin_user = super_user1.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admintest',
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@gmail.com')

        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)


class SignupTests(TestCase):
    def setUp(self):
        self.username = 'newuser'
        self.email = 'newuser@gmail.com'
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, new_user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, new_user.email)

        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)
