from src.models.customer import CustomerModel
from src.models.sale import SaleModel
from tests.base_test import BaseTest


class CustomerTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')

            self.assertIsNone(CustomerModel.find_by_name('test_first_name','test_last_name'), "Found an customer with name 'test_first_name' before save_to_db")

            customer.save_to_db()

            self.assertIsNotNone(CustomerModel.find_by_name('test_first_name','test_last_name'),
                                 "Did not find an customer with name 'test_first_nametest_last_name' after save_to_db")

            customer.delete_from_db()

            self.assertIsNone(CustomerModel.find_by_name('test_first_name','test_last_name'), "Found an customer with name 'test_first_nametest_last_name' after delete_from_db")

    def test_customer_relationship(self):
        with self.app_context():
            customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
            sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status',customer.id)

            customer.save_to_db()
            sale.save_to_db()

            self.assertEqual(customer.sales.count(), 1)
            self.assertEqual(customer.sales.first().date, sale.date)
