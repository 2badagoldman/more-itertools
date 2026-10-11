from unittest import TestCase

import more_itertools as mi


class BucketMissingKeyTests(TestCase):
    key = staticmethod(lambda x: 10 * (x // 10))

    def test_contains_does_not_invent(self):
        D = mi.bucket([10, 20, 11, 21], key=self.key)
        self.assertNotIn(30, D)
        self.assertEqual(set(D), {10, 20})

    def test_getitem_does_not_invent(self):
        D = mi.bucket([10, 20, 11, 21], key=self.key)
        self.assertEqual(list(D[30]), [])
        self.assertNotIn(30, D)
        self.assertEqual(set(D), {10, 20})

    def test_permissive_validator(self):
        D = mi.bucket([10, 20, 11, 21], self.key, lambda x: True)
        self.assertNotIn(30, D)
        self.assertEqual(list(D[30]), [])
        self.assertEqual(list(D[10]), [10, 11])
        self.assertEqual(set(D), {10, 20})

    def test_empty(self):
        D = mi.bucket([], key=lambda x: x)
        self.assertNotIn(1, D)
        self.assertEqual(list(D[1]), [])
        self.assertEqual(list(D), [])
