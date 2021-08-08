from django.test import TestCase
from django.urls import reverse

from blog.models import postagem, autor


class PostagemListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        numero_de_postagens = 8

        for postagem_id in range(numero_de_postagens):
            postagem.objects.create(
                titulo=f'teste {postagem_id}', autor=autor.objects.create(
                    nome='Andre')
            )

    def test_url_view_esta_no_local_certo(self):
        response = self.client.get('/blog/postagens/')
        self.assertEqual(response.status_code, 200)

    def test_url_view_acessivel_por_nome(self):
        response = self.client.get(reverse('postagens'))
        self.assertEqual(response.status_code, 200)

    def test_view_usa_template_correta(self):
        response = self.client.get(reverse('postagens'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/postagem_list.html')

    def test_5_postagens_por_pagina(self):
        response = self.client.get(reverse('postagens'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['postagem_list']), 5)

    def test_ultima_pagina_tem_3(self):
        response = self.client.get(reverse('postagens')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['postagem_list']), 3)
