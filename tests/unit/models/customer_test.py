from src.models.customer import CustomerModel
from tests.base_test import BaseTest


class CustomerTest(BaseTest):
    def test_create_customer(self):
        customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')

        self.assertEqual(customer.first_name, 'test_first_name',
                         "The test_first_name of the customer after creation does not equal the constructor argument.")
        self.assertListEqual(customer.sales.all(), [],
                             "The customer's sales length was not 0 even though no sales were added.")


    def test_customer_json(self):

        customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
        expected = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'phone': '050-0000000',
            'email': 'test@gmail.com',
            'city': 'test_city',
            'address': 'test_address',
            'birth_date': '01-01-2019'
        }


        self.assertEqual(
            customer.json(),
            expected,
            "The JSON export of the customer is incorrect. Received {}, expected {}.".format(customer.json(), expected))

        # def test_customer_validation(self):
        #     customer = CustomerModel('test_first_name', 'test_last_name', '050-0000000', 'test@gmail.com', 'test_city',
        #                              'test_address', '01-01-2019')
        #
