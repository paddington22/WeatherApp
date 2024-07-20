from django.test import TestCase, Client

from homepage.models import QueryHistory, Device


class QueryHistoryTemplateViewTestCase(TestCase):
    def test_respone(self):
        client = Client()
        response = client.get('/history/')
        self.assertEqual(response.status_code, 200)
        response = client.post('/history/')
        self.assertEqual(response.status_code, 405)

    def test_content_less_than_10(self):
        device = Device.objects.create()
        for i in range(6):
            QueryHistory.objects.create(device=device, query='Moscow')
        client = Client()
        response = client.get('/history/', headers={'Cookie': 'device=1'})
        context = response.context
        self.assertEqual(len(context['object_list']), 6)
        self.assertEqual((context['count']), 6)

    def test_content_more_than_10(self):
        device = Device.objects.create()
        for i in range(25):
            QueryHistory.objects.create(device=device, query='Moscow')
        client = Client()
        response = client.get('/history/', headers={'Cookie': 'device=1'})
        context = response.context
        self.assertEqual(len(context['object_list']), 10)
        self.assertEqual((context['count']), 10)


class HomepageTemplateViewTestCase(TestCase):
    def test_response(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.client.cookies['device'].value, '1')
        response = client.post('/')
        self.assertEqual(response.status_code, 200)
