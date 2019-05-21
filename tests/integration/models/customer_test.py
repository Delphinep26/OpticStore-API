from models.customer import CustomerModel
from models.sale import SaleModel
from tests.base_test import BaseTest


class CustomerTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            customer = CustomerModel('test','test' ,'0544881606','delphine-elfassi@hotmail.com','Netanya',birth_date='26-05-1990')

            self.assertIsNone(CustomerModel.find_by_name('test','test'), "Found an customer with name 'test' before save_to_db")

            customer.save_to_db()

            self.assertIsNotNone(CustomerModel.find_by_name('test','test'),
                                 "Did not find an customer with name 'test' after save_to_db")

            customer.delete_from_db()

            self.assertIsNone(CustomerModel.find_by_name('test','test'), "Found an customer with name 'test' after delete_from_db")

    def test_customer_relationship(self):
        with self.app_context():
            customer = CustomerModel('test_customer','test_customer' ,'0544881606','delphine-elfassi@hotmail.com','Netanya',birth_date='26-05-1990')
            sale = SaleModel(date='20-05-2019',total_price=200,payment_type='check', status = 'Closed',cust_id ='1')

            customer.save_to_db()
            sale.save_to_db()

            self.assertEqual(customer.sales.count(), 1)
            self.assertEqual(customer.sales.first().date, sale.date)
