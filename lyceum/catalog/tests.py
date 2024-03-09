from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_converter(self):
        response = Client().get('/catalog/converter/1/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re0(self):
        response = Client().get('/catalog/re/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re1(self):
        response = Client().get('/catalog/re/1/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_re01(self):
        response = Client().get('/catalog/re/01/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re010(self):
        response = Client().get('/catalog/re/010/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re10(self):
        response = Client().get('/catalog/re/10/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_re100(self):
        response = Client().get('/catalog/re/100/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_re00(self):
        response = Client().get('/catalog/re/-0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re21(self):
        response = Client().get('/catalog/re/-21/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re000(self):
        response = Client().get('/catalog/re/0.1/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re100rrr(self):
        response = Client().get('/catalog/re/r3rr100rrr7/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_re100spec(self):
        response = Client().get('/catalog/re/100$/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re0(self):
        response = Client().get('/catalog/converter/0/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re1(self):
        response = Client().get('/catalog/converter/1/')
        self.assertEqual(response.status_code, 200)

    def test_converter_re01(self):
        response = Client().get('/catalog/re/01/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re010(self):
        response = Client().get('/catalog/re/010/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re10(self):
        response = Client().get('/catalog/re/10/')
        self.assertEqual(response.status_code, 200)

    def test_converter_re100(self):
        response = Client().get('/catalog/re/100/')
        self.assertEqual(response.status_code, 200)

    def test_converter_re00(self):
        response = Client().get('/catalog/re/-0/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re21(self):
        response = Client().get('/catalog/re/-21/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re000(self):
        response = Client().get('/catalog/re/0.1/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re100rrr(self):
        response = Client().get('/catalog/re/r3rr100rrr7/')
        self.assertEqual(response.status_code, 404)

    def test_converter_re100spec(self):
        response = Client().get('/catalog/re/100$/')
        self.assertEqual(response.status_code, 404)
