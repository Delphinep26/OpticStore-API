from src.models.sale import SaleModel
from src.models.customer import CustomerModel
from tests.base_test import BaseTest
import json


class CustomerTest(BaseTest):
    def test_customer_not_found(self):
        with self.app() as c:
            r = c.get('/customer/test')
            self.assertEqual(r.status_code, 404)

    def test_customer_found(self):
        with self.app() as c:
            with self.app_context():
                CustomerModel('test').save_to_db()
                r = c.get('/customer/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'sales': []},
                                     d2=json.loads(r.data))

    def test_customer_with_sales_found(self):
        with self.app() as c:
            with self.app_context():
                CustomerModel('test').save_to_db()
                SaleModel('test', 2.99, 1).save_to_db()
                r = c.get('/customer/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'sales': [{'name': 'test', 'price': 2.99}]},
                                     d2=json.loads(r.data))

    def test_delete_customer(self):
        with self.app() as c:
            with self.app_context():
                CustomerModel('test').save_to_db()
                r = c.delete('/customer/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'customer deleted'},
                                     d2=json.loads(r.data))

    def test_create_customer(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/customer/test')

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(CustomerModel.find_by_name('test'))
                self.assertDictEqual(d1={'name': 'test', 'sales': []},
                                     d2=json.loads(r.data))

    def test_create_duplicate_customer(self):
        with self.app() as c:
            with self.app_context():
                c.post('/customer/test')
                r = c.post('/customer/test')

                self.assertEqual(r.status_code, 400)

    def test_customer_list(self):
        with self.app() as c:
            with self.app_context():
                CustomerModel('test').save_to_db()
                r = c.get('/customers')

                self.assertDictEqual(d1={'customers': [{'name': 'test', 'sales': []}]},
                                     d2=json.loads(r.data))

    def test_customer_with_sales_list(self):
        with self.app() as c:
            with self.app_context():
                CustomerModel('test').save_to_db()
                SaleModel('test', 17.99, 1).save_to_db()
                r = c.get('/customers')

                self.assertDictEqual(d1={'customers': [{'name': 'test', 'sales': [{'name': 'test', 'price': 17.99}]}]},
                                     d2=json.loads(r.data))
