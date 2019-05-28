
from src.models.sale import SaleModel
from tests.base_test import BaseTest
import json


class SaleTest(BaseTest):
    def setUp(self):
        super(SaleTest, self).setUp()
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                auth_request = c.post('/auth', data=json.dumps({
                    'username': 'test_username',
                    'password': 'A12345678'
                }), headers={'Content-Type': 'application/json'})
                self.auth_header = "JWT {}".format(json.loads(auth_request.data)['access_token'])

    def test_sale_no_auth(self):
        with self.app() as c:
            r = c.get('/sale/1')
            self.assertEqual(r.status_code, 401)

    def test_sale_not_found(self):
        with self.app() as c:
            r = c.get('/sale/1', headers={'Authorization': self.auth_header})
            self.assertEqual(r.status_code, 404)

    def test_sale_found(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                r = c.get('/sale/1', headers={'Authorization': self.auth_header})
                expected = {'date': '01-01-2019',
                            'total price': 100,
                            'payment_type': 'test_payment_type',
                            'status': 'test_status',
                            'customer_id': '1',
                            }
                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1=expected,
                                     d2=json.loads(r.data))

    def test_delete_sale(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                r = c.delete('/sale/1')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'Sale deleted'},
                                     d2=json.loads(r.data))

    def test_create_item(self):
        with self.app() as c:
            with self.app_context():

                sale_data = {'date': '01-01-2019',
                            'total price': 100,
                            'payment_type': 'test_payment_type',
                            'status': 'test_status',
                            'customer_id': '1',
                            }
                r = c.post('/sale', data=sale_data)

                self.assertEqual(r.status_code, 201)
                self.assertEqual(SaleModel.find_by_date('01-01-2019','1').total_price, 100)
                self.assertDictEqual(d1=sale_data,
                                     d2=json.loads(r.data))

    def test_create_duplicate_item(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                sale_data = {'date': '01-01-2019',
                             'total price': 100,
                             'payment_type': 'test_payment_type',
                             'status': 'test_status',
                             'customer_id': '1',
                             }
                c.post('/sale', data=sale_data)
                r = c.post('/sale', data=sale_data)

                self.assertEqual(r.status_code, 400)

    def test_put_item(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                sale_data = {'date': '01-01-2019',
                             'total price': 100,
                             'payment_type': 'test_payment_type',
                             'status': 'test_status',
                             'customer_id': '1',
                             }
                r = c.put('/sale', data=sale_data)

                self.assertEqual(r.status_code, 200)
                self.assertEqual(SaleModel.find_by_date('01-01-2019','1').total_price, 100)
                self.assertDictEqual(d1=sale_data,
                                     d2=json.loads(r.data))

    def test_put_update_item(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                sale_data = {'date': '01-01-2019',
                             'total price': 100,
                             'payment_type': 'test_payment_type',
                             'status': 'test_status',
                             'customer_id': '1',
                             }
                c.put('/sale', data=sale_data)
                r = c.put('/sale/1', data=sale_data)

                self.assertEqual(r.status_code, 200)
                self.assertEqual(SaleModel.find_by_date('01-01-2019','1').total_price, 100)

    def test_item_list(self):
        with self.app() as c:
            with self.app_context():
                sale = SaleModel('01-01-2019', 100, 'test_payment_type', 'test_status', '1')
                sale.save_to_db()
                r = c.get('/sales')
                sale_data = {'date': '01-01-2019',
                             'total price': 100,
                             'payment_type': 'test_payment_type',
                             'status': 'test_status',
                             'customer_id': '1',
                             }

                self.assertDictEqual(d1={'sales': sale_data},
                                     d2=json.loads(r.data))
