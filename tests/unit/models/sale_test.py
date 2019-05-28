from src.models.sale import SaleModel
from tests.base_test import BaseTest


class SaleTest(BaseTest):

    def test_create_sale(self):

        sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status','1')

        self.assertEqual(sale.date, '01-01-2019',
                         "The date of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.total_price, 100,
                         "The total price of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.payment_type, 'test_payment_type',
                         "The payment_type of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.status,'test_status',  "The status of the sale after creation does not equal the constructor argument.")
        self.assertEqual(sale.customer_id,'1',"The customer_id of the sale after creation does not equal the constructor argument.")

    def test_sale_json(self):
        sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')

        expected = {'date': '01-01-2019',
                    'total price': 100,
                    'payment_type': 'test_payment_type',
                    'status': 'test_status',
                    'customer_id': '1',
                    }

        self.assertEqual(
            sale.json(),
            expected,
            "The JSON export of the sale is incorrect. Received {}, expected {}.".format(sale.json(), expected))
