from src.models.customer import CustomerModel
from src.models.sale import SaleModel
from tests.base_test import BaseTest


class SaleTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status','1')

            self.assertIsNone(SaleModel.find_by_date('01-01-2019','1'), "Found an sale in date '01-01-2019' for cust '1'  before save_to_db")

            sale.save_to_db()

            self.assertIsNotNone(CustomerModel.find_by_name('1').sales.find_by_date('01-01-2019','1'),
                                 "Did not find an sale with date '01-01-2019' for cust '1' after save_to_db")

            sale.delete_from_db()

            self.assertIsNone(SaleModel.find_by_date('01-01-2019','1'), "Found an sale with date '01-01-2019' for cust '1' after delete_from_db")

            self.assertIsNone(CustomerModel.find_by_name('1').sales.find_by_date('01-01-2019','1'), "Found an sale with date '01-01-2019' for cust '1' after delete_from_db")

    def test_customer_relationship(self):
        with self.app_context():
            customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
            sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status',customer.id)

            customer.save_to_db()
            sale.save_to_db()

            self.assertEqual(sale.cust_id, customer.id)
