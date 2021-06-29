
import Circle
import unittest
from math import pi
import logging



class UnitTest_Quiz(unittest.TestCase):
    def run_test(self):

       #create object class Circle
        cir = Circle.Circle()

        logging.warning('Warning:You enter in the testing phase')
        print("You enter in the testing phase")
        print("sample input to check program\n  enter radius :1 \n Enter area of circle:3.14 \n Enter area of circle_diameter according to above radius:2 \n Enter area of circle_circumference according to above radius:6.28")

        min=1
        max=1000
        logging.error('radius value  less than %d and area greater than %d generate error ',min,max)
        print(f" radius value less than {min} and area greater than {max} generate error")
        r=int(input("enter radius: "))
        area = float(input("Enter area of circle:"))


        #apply all class on circle_area method
        self.assertAlmostEqual(cir.circle_area(r),area) # assertAlmostEqual method raised when value is not equal
        self.assertEqual(cir.circle_area(r), area)      # assertEqual method raised error when value is not equal
        self.assertNotEqual(cir.circle_area(r), 1, "fail")   # assertNotEqual method raised error when value is  equal
        self.assertGreater(cir.circle_area(r), 1)          #assertGreater  method is raised error when  value is not greater
        self.assertLess(cir.circle_area(r),1000)            # assertLess  method is raised error when  value is not Less
        print("correct")

        # apply all class on circle_diameter method

        logging.error('radius value  less than %d and circle_diameter greater than %d generate error ', min, max)
        print(f" radius value less than {min} and circle_diameter greater than {max} generate error")
        diameter=float(input("Enter area of circle_diameter according to above radius:"))
        self.assertAlmostEqual(cir.circle_diameter(r),diameter)   # assertAlmostEqual method raised when value is not equal
        self.assertEqual(cir.circle_diameter(r), diameter)      # assertEqual method raised error when value is not equal
        self.assertNotEqual(cir.circle_diameter(r), 3, "fail")   # assertNotEqual method raised error when value is  equal
        self.assertGreater(cir.circle_diameter(r), 1)           #assertGreater  method is raised error when  value is not greater
        self.assertLess(cir.circle_diameter(r), 1000)           # assertLess  method is raised error when  value is not Less
        print("correct")

        # apply all class on circle_circumference method

        logging.error('radius value  less than %d and circle_circumference greater than %d generate error ', min, max)
        print(f" radius value less than {min} and circle_circumference greater than {max} generate error")
        circumference = float(input("Enter area of circle_circumference according to above radius"))
        self.assertAlmostEqual(cir.circle_circumference(r),circumference) # assertAlmostEqual method raised when value is not equal
        self.assertEqual(cir.circle_circumference(r),circumference) # assertEqual method raised error when value is not equal
        self.assertNotEqual(cir.circle_circumference(r),6,"fail")    # assertNotEqual method raised error when value is  equal
        self.assertGreater(cir.circle_circumference(r), 1)  #assertGreater  method is raised error when  value is not greater
        self.assertLess(cir.circle_circumference(r),1000)  # assertLess  method is raised error when  value is not Less

        #assertTrue
        self.assertTrue(cir.true_false(2),"Fail")
        self.assertTrue(cir.true_false(10), "Fail")
        self.assertTrue(cir.true_false(12), "Fail")
        #assertFalse

        self.assertFalse(cir.true_false(0), "Fail")
        self.assertFalse(cir.true_false(0), "Fail")
        self.assertFalse(cir.true_false(0), "Fail")

        # value errors are raised when necessary using assertRaises method
       # self.assertRaises(ValueError, cir.circle_area, -2)'''
