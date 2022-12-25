import unittest
from db.config import read_sql

class TestReadSQL(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_sql(self):
        path = 'src/tests/test.sql'
        sql = read_sql(path)
        self.assertEqual(sql, 'TEST')
