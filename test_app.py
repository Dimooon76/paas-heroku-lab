import unittest
from app import app, APP_VERSION


class TestApp(unittest.TestCase):
    def test_index(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Версия {APP_VERSION}'.encode('utf-8'), response.data)

    def test_health(self):
        response = app.test_client().get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok', 'version': APP_VERSION})


if __name__ == '__main__':
    unittest.main()
