import unittest
import Ex1_6_1
import Ex1_6_2
import Ex1_6_3
import Ex1_6_4
import Ex2_1_1
import Ex2_1_2
import Ex2_2_1
import Ex2_2_2
import Ex2_2_3
import Ex2_3_1
import Ex2_3_2
import Ex2_4_1

class TestAbs(unittest.TestCase):
    
    def test_161(self):
        click = Ex1_6_1.test_1_6_1()
        self.assertEqual(click, None, "Not click to the button")

    def test_162(self):
        click = Ex1_6_2.test_1_6_2()
        self.assertEqual(click, None, "Not click to the button")
        
    def test_163(self):
        click = Ex1_6_3.test_1_6_3()
        self.assertEqual(click, None, "Not click to the button")

    def test_164(self):
        click = Ex1_6_4.test_1_6_4()
        self.assertEqual(click, None, "Not click to the button")

    def test_211(self):
        click = Ex2_1_1.test_2_1_1()
        self.assertEqual(click, None, "Not click to the button") 

    def test_212(self):
        click = Ex2_1_2.test_2_1_2()
        self.assertEqual(click, None, "Not click to the button")

    def test_221(self):
        click = Ex2_2_1.test_2_2_1()
        self.assertEqual(click, None, "Not click to the button")

    def test_222(self):
        click = Ex2_2_2.test_2_2_2()
        self.assertEqual(click, None, "Not click to the button")     

    def test_223(self):
        click = Ex2_2_3.test_2_2_3()
        self.assertEqual(click, None, "Not click to the button")
    
    def test_231(self):
        click = Ex2_3_1.test_2_3_1()
        self.assertEqual(click, None, "Not click to the button")
    
    def test_232(self):
        click = Ex2_3_2.test_2_3_2()
        self.assertEqual(click, None, "Not click to the button")

    def test_241(self):
        click = Ex2_4_1.test_2_4_1()
        self.assertEqual(click, None, "Not click to the button")


if __name__ == "__main__":
    unittest.main()
