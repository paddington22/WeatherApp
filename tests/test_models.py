from django.test import TestCase
from homepage.models import Device, QueryHistory
from api.models import Statistic


class DeviceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Device.objects.create(last_query='Moscow')

    def test_last_query_label(self):
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('last_query').verbose_name
        self.assertEqual(field_label, 'Введите название города')

    def test_last_query_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('last_query').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_id(self):
        device = Device.objects.get(id=1)
        expected_object_name = str(device.id)
        self.assertEqual(expected_object_name, str(device))


class QueryHistoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        device = Device.objects.create(last_query='Moscow')
        QueryHistory.objects.create(device=device, query='Moscow')

    def test_device_label(self):
        query = QueryHistory.objects.get(id=1)
        field_label = query._meta.get_field('device').verbose_name
        self.assertEqual(field_label, 'device')

    def test_query_label(self):
        query = QueryHistory.objects.get(id=1)
        field_label = query._meta.get_field('query').verbose_name
        self.assertEqual(field_label, 'query')

    def test_query_max_length(self):
        query = QueryHistory.objects.get(id=1)
        max_length = query._meta.get_field('query').max_length
        self.assertEqual(max_length, 100)


class StatisticTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Statistic.objects.create(city='Moscow', count=1)

    def test_city_label(self):
        statistic = Statistic.objects.get(id=1)
        field_label = statistic._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_city_max_lebgth(self):
        statistic = Statistic.objects.get(id=1)
        max_length = statistic._meta.get_field('city').max_length
        self.assertEqual(max_length, 100)

    def test_count_label(self):
        statistic = Statistic.objects.get(id=1)
        field_label = statistic._meta.get_field('count').verbose_name
        self.assertEqual(field_label, 'count')
