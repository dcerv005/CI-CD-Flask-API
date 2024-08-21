import unittest
from app import app
from faker import Faker

class TestAPI(unittest.TestCase):
    def setup(self):
        self.app = app.test_client()

    def test_negative_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        num1 = 0-num1
        num2 = 0-num2
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], num1 + num2)

if __name__ == '__main__':
    unittest.main()