import app
import unittest
import pandas as pd

class appTest(unittest.TestCase):

    def test1(self): 
        answer = pd.Series(['фамилия', 'класс', 'подгруппа', 'предмет', 'видДеятельности'])
        data = app.get_data('./pr1.json')
        self.assertEqual(app.main(data), answer)

    def test2(self): 
        answer = pd.Series(['класс', 'предмет'])
        data = app.get_data('./pr2.json')
        self.assertEqual(app.main(data), answer)
        

if __name__ == "__main__":
    unittest.main()
        




