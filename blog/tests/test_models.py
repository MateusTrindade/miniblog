from django.test import TestCase

# Create your tests here.

from blog.models import autor


class AutorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        autor.objects.create(nome='Lara', bio='Nova autora')

    def test_nome_label(self):
        autor1 = autor.objects.get(id=1)
        field_label = autor1._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')

    def test_bio_label(self):
        autor1 = autor.objects.get(id=1)
        field_label = autor1._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_data_registro_label(self):
        autor1 = autor.objects.get(id=1)
        field_label = autor1._meta.get_field('data_registro').verbose_name
        self.assertEqual(field_label, 'data registro')

    def test_nome_max_length(self):
        autor1 = autor.objects.get(id=1)
        max_length = autor1._meta.get_field('nome').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        autor1 = autor.objects.get(id=1)
        self.assertEqual(autor1.get_absolute_url(), '/blog/autor/1/')

    def test__str__(self):
        autor1 = autor.objects.get(id=1)
        self.assertEqual(autor1.__str__(), 'Lara')
