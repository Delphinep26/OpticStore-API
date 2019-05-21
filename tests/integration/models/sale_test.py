from src.models.customer import CustomerModel
from src.models.sale import SaleModel
from tests.base_test import BaseTest


class SaleTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            sale = SaleModel('test')
            sale.save_to_db()
            sale = SaleModel('test', 19.99, 1)

            self.assertIsNone(SaleModel.find_by_name('test'), "Found an customer with sale 'test' before save_to_db")

            sale.save_to_db()

            self.assertIsNotNone(CustomerModel.find_by_name('test'),
                                 "Did not find an sale with name 'test' after save_to_db")

            sale.delete_from_db()

            self.assertIsNone(CustomerModel.find_by_name('test'), "Found an sale with name 'test' after delete_from_db")

    def test_customer_relationship(self):
        with self.app_context():
            customer = CustomerModel('test_customer')
            sale = SaleModel('test', 19.99, 1)

            customer.save_to_db()
            sale.save_to_db()

            self.assertEqual(sale.store.name, 'test_customer')
