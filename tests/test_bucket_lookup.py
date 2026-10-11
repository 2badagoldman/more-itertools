from unittest import TestCase

import more_itertools as mi


class BucketLookupTests(TestCase):
    def setUp(self):
        self.iterable = [10, 20, 11, 21]
        self.key = lambda x: 10 * (x // 10)

    def test_contains_does_not_invent_keys(self):
        D = mi.bucket(self.iterable, key=self.key)
        self.assertNotIn(30, D)
        self.assertEqual(set(D), {10, 20})

    def test_getitem_does_not_invent_keys(self):
        D = mi.bucket(self.iterable, key=self.key)
        self.assertEqual(list(D[30]), [])
        self.assertEqual(set(D), {10, 20})

    def test_validator_accepting_missing_key(self):
        D = mi.bucket(self.iterable, key=self.key, validator=lambda x: True)
        self.assertNotIn(30, D)
        self.assertEqual(list(D[30]), [])
        self.assertEqual(set(D), {10, 20})

    def test_consumed_key_still_listed(self):
        D = mi.bucket(self.iterable, key=self.key)
        self.assertEqual(list(D[10]), [10, 11])
        self.assertNotIn(30, D)
        self.assertEqual(set(D), {10, 20})

    def test_empty(self):
        D = mi.bucket([], key=self.key)
        self.assertNotIn(10, D)
        self.assertEqual(list(D[10]), [])
        self.assertEqual(list(D), [])
