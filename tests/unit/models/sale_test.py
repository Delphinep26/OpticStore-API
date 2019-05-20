from models.sale import SaleModel
from tests.base_test import BaseTest


class SaleTest(BaseTest):
    def test_create_sale(self):
        sale = SaleModel('test', 19.99, 1)

        self.assertEqual(sale.name, 'test',
                         "The name of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.price, 19.99,
                         "The price of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.store_id, 1,
                         "The store_id of the sale after creation does not equal the constructor argument.")
        self.assertIsNone(sale.store, "The sale's store was not None even though the store was not created.")

    def test_sale_json(self):
        sale = SaleModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            sale.json(),
            expected,
            "The JSON export of the sale is incorrect. Received {}, expected {}.".format(sale.json(), expected))
