from unittest import TestCase

import more_itertools as mi


class BucketMissingKeyTests(TestCase):
    def test_missing_key_not_invented(self):
        key = lambda x: 10 * (x // 10)
        for validator in (None, lambda x: x in {10, 20, 30}):
            with self.subTest(validator=validator):
                D = mi.bucket([10, 20, 11, 21], key, validator=validator)
                self.assertNotIn(30, D)
                self.assertEqual(set(D), {10, 20})

                D = mi.bucket([10, 20, 11, 21], key, validator=validator)
                self.assertEqual(list(D[30]), [])
                self.assertEqual(set(D), {10, 20})

    def test_existing_key_after_missing_lookup(self):
        D = mi.bucket([10, 20, 11, 21], key=lambda x: 10 * (x // 10))
        self.assertNotIn(30, D)
        self.assertEqual(list(D[30]), [])
        self.assertEqual(list(D[10]), [10, 11])
        self.assertEqual(list(D[20]), [20, 21])
