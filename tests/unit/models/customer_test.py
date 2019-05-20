from models.customer import CustomerModel
from tests.base_test import BaseTest


class CustomerTest(BaseTest):
    def test_create_customer(self):
        customer = CustomerModel('test')

        self.assertEqual(customer.name, 'test',
                         "The name of the customer after creation does not equal the constructor argument.")
        self.assertListEqual(customer.items.all(), [],
                             "The customer's items length was not 0 even though no items were added.")

    def test_customer_json(self):
        customer = CustomerModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(
            customer.json(),
            expected,
            "The JSON export of the customer is incorrect. Received {}, expected {}.".format(customer.json(), expected))
