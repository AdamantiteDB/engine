import unittest
from unittest import runner
from tests import query as query_tests

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    query_test_suite = unittest.defaultTestLoader.loadTestsFromModule(
        query_tests)

    runner.run(query_test_suite)
