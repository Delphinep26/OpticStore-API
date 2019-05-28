from src.models.sale import SaleModel
from src.models.customer import CustomerModel
from tests.base_test import BaseTest
import json


class CustomerTest(BaseTest):
    def test_customer_not_found(self):
        with self.app() as c:
            r = c.get('/customer/1')
            self.assertEqual(r.status_code, 404)

    def test_customer_found(self):
        with self.app() as c:
            with self.app_context():
                customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
                customer.save_to_db()
                r = c.get('/customer/1')

                self.assertEqual(r.status_code, 200)
                expected = {
                            'first_name': 'test_first_name',
                            'last_name': 'test_last_name',
                            'phone': '050-0000000',
                            'email': 'test@gmail.com',
                            'city': 'test_city',
                            'address': 'test_address',
                            'birth_date': '01-01-2019'
                            }
                self.assertDictEqual(d1=expected,
                                     d2=json.loads(r.data))

    def test_customer_with_sales_found(self):
        with self.app() as c:
            with self.app_context():
                customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
                customer.save_to_db()
                sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status','1')
                sale.save_to_db()
                r = c.get('/customer/1/sales')

                self.assertEqual(r.status_code, 200)
                expected = {'date': '01-01-2019',
                    'total price': 100,
                    'payment_type': 'test_payment_type',
                    'status': 'test_status',
                    'customer_id': '1',
                    }
                self.assertDictEqual(d1=expected,
                                     d2=json.loads(r.data))

    def test_delete_customer(self):
        with self.app() as c:
            with self.app_context():
                customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
                customer.save_to_db()
                r = c.delete('/customer/1')
                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'customer deleted'},
                                     d2=json.loads(r.data))

    def test_create_customer(self):
        with self.app() as c:
            with self.app_context():
                json_customer = {
                    'first_name': 'test_first_name',
                    'last_name': 'test_last_name',
                    'phone': '050-0000000',
                    'email': 'test@gmail.com',
                    'city': 'test_city',
                    'address': 'test_address',
                    'birth_date': '01-01-2019'
                }
                r = c.post('/customer' , json=json_customer)

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(CustomerModel.find_by_name('test_first_name','test_last_name'))
                self.assertDictEqual(d1=json_customer,
                                     d2=json.loads(r.data))

    def test_create_duplicate_customer(self):
        with self.app() as c:
            with self.app_context():
                json_customer = {
                    'first_name': 'test_first_name',
                    'last_name': 'test_last_name',
                    'phone': '050-0000000',
                    'email': 'test@gmail.com',
                    'city': 'test_city',
                    'address': 'test_address',
                    'birth_date': '01-01-2019'
                }
                r = c.post('/customer' , json=json_customer)

                self.assertEqual(r.status_code, 400)

    def test_customer_list(self):
        with self.app() as c:
            with self.app_context():
                customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
                                 'test_address','01-01-2019')
                customer.save_to_db()
                r = c.get('/customers')
                expected = {
                            'first_name': 'test_first_name',
                            'last_name': 'test_last_name',
                            'phone': '050-0000000',
                            'email': 'test@gmail.com',
                            'city': 'test_city',
                            'address': 'test_address',
                            'birth_date': '01-01-2019'
                            }

                self.assertDictEqual(d1=expected,
                                     d2=json.loads(r.data))

##    def test_customer_with_sales_list(self):
##        with self.app() as c:
##            with self.app_context():
##                customer = CustomerModel('test_first_name','test_last_name','050-0000000','test@gmail.com','test_city',
##                                 'test_address','01-01-2019')
##                customer.save_to_db()
##                sale = SaleModel('01-01-2019', 100, 'test_payment_type','test_status','1')
##                sale.save_to_db()
##                r = c.get('/customers')
##
##                self.assertDictEqual(d1={'customers': [{'name': 'test', 'sales': [{'name': 'test', 'price': 17.99}]}]},
##                                     d2=json.loads(r.data))
