
'''
god i hate math
'''

import unittest

from lithicrivers.model.vector import VectorN


class TestVectorN(unittest.TestCase):
    def testSimple(self):
        # foosdfasdf
        v1 = VectorN(1, 2, 0)
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 0)
        self.assertEqual(v1.w, None)

        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[1], 2)
        self.assertEqual(v1[2], 0)

        daError = "Didn't throw error."
        try:
            self.assertEqual(v1[3], None)
        except IndexError as e:
            daError = e
        finally:
            self.assertIsInstance(daError, IndexError)

    def testSerialize(self):
        v1 = VectorN(1, 2, 3, 4)
        self.assertEqual(v1.serialize(), '1,2,3,4')
        self.assertEqual(VectorN.deserialize('1,2,3,4'), v1)

        v2 = VectorN(1)
        self.assertEqual(v2.serialize(), '1')
        self.assertEqual(VectorN.deserialize('1'), v2)

    def testMath(self):
        v1 = VectorN(1, 2, 3)

        self.assertEqual(v1 + v1, VectorN(2, 4, 6))
        self.assertEqual(v1 - v1, VectorN(0, 0, 0))
        self.assertEqual(v1 * v1, VectorN(1, 4, 9))

    def testVectorTrim(self):
        v1 = VectorN(1, 2, 3).trim(2)
        v2 = VectorN(1, 2)

        # print(v1)
        # print(v2)

        self.assertEqual(v1, v2)

    def testVecNBoundingBox(self):
        v1 = VectorN(1, 2)
        v2 = VectorN(6, 7)

        v3 = VectorN(4, 4)

        v4 = VectorN(1, 9)

        self.assertTrue(v3.inside_bounding_rect(v1, v2))
        # swap args shouldnt matter, it just flips the rect by 90 degrees
        self.assertTrue(v3.inside_bounding_rect(v2, v1))

        self.assertFalse(v4.inside_bounding_rect(v1, v2))
        self.assertFalse(v4.inside_bounding_rect(v2, v1))
