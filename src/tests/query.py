import unittest

from helpers.query import Query


QUERY_MOCK = {
    'table_name': 'Users',
    'equals_to': [['name', 'Hideki'], ['id', 0]],
    'starts_with': [['name', 'H']]
}


class TestQuery(unittest.TestCase):

    def test_inheritance(self):
        query_obj = Query(QUERY_MOCK)
        self.assertIsInstance(query_obj, Query)

    def test_table_name(self):
        query_obj = Query(QUERY_MOCK)
        self.assertIsNotNone(getattr(query_obj, 'table_name'))

    def test_equals_to(self):
        query_obj = Query(QUERY_MOCK)
        self.assertIsNotNone(getattr(query_obj, 'equals_to'))
        self.assertIsInstance(getattr(query_obj, 'equals_to'), list)

    def test_starts_with(self):
        query_obj = Query(QUERY_MOCK)
        self.assertIsNotNone(getattr(query_obj, 'starts_with'))
        self.assertIsInstance(getattr(query_obj, 'starts_with'), list)
