from django.test import TestCase, Client
from django.urls import reverse

class UrlsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # redireciona para login se não logado

    def test_listar_contatos_login_required(self):
        response = self.client.get(reverse('listar_contatos'))
        self.assertEqual(response.status_code, 302)  # deve redirecionar para login
