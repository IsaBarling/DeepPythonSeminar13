import unittest
from circle_area import InvalidRadiusTypeError, NegativeRadiusError, circle_area
from math import pi

R1 = "Radius can't be negative"
R2 = "Radius must be a non-negative real number only"



class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(3), pi * 3 ** 2)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi * 2.5 ** 2)

    def test_values(self):
        with self.assertRaises(NegativeRadiusError) as context:
            circle_area(-2)
        self.assertEqual(str(context.exception), R1)

        with self.assertRaises(NegativeRadiusError) as context:
            circle_area(-1)
        self.assertEqual(str(context.exception), R1)

    def test_types(self):
        with self.assertRaises(InvalidRadiusTypeError) as context:
            circle_area(5 + 2j)
        self.assertEqual(str(context.exception), R2)

        with self.assertRaises(InvalidRadiusTypeError) as context:
            circle_area("five")
        self.assertEqual(str(context.exception), R2)

        with self.assertRaises(InvalidRadiusTypeError) as context:
            circle_area([16, 22])
        self.assertEqual(str(context.exception), R2)

        with self.assertRaises(InvalidRadiusTypeError) as context:
            circle_area([42])
        self.assertEqual(str(context.exception), R2)

        with self.assertRaises(InvalidRadiusTypeError) as context:
            circle_area(True)
        self.assertEqual(str(context.exception), R2)


if __name__ == "__main__":
    unittest.main()
