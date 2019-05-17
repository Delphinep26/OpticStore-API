# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\Delphine\PycharmProjects\MyProj\src\resources\sale.py
# Compiled at: 2019-05-14 23:10:34
# Size of source mod 2**32: 4044 bytes
"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.sale import SaleModel


class Sale(Resource):
    """Sales Order' endpoint."""
    parser = reqparse.RequestParser()
    parser.add_argument('date',
                        type=str,
                        required=False,
                        help='Date in the format yyyymmdd')
    parser.add_argument('total_price',
                        type=int,
                        required=True,
                        help='Every sales needs a price.')
    parser.add_argument('payment_type',
                        type=str,
                        required=True,
                        help='Every sales needs a payment type.')
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help='Every sales needs a status.')
    parser.add_argument('cust_id',
                        type=str,
                        required=True,
                        help='Every sales needs a cust_id.')

    @jwt_required()
    def get(self, id):
        """
        Finds an item by its name and returns it.

        :param id: the id of the sale order.
        :type str
        :return: item data.
        :rtype: application/json.
        """
        sale_order = SaleModel.find_by_id(id)
        if sale_order:
            return sale_order.json()
        else:
            return (
                {'message': 'sale order not found'}, 404)

    def post(self):
        """
        Creates a new item using the provided name, price and store_id.

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Sale.parser.parse_args()
        sale_order = SaleModel(**request_data)
        try:
            sale_order.save_to_db()
        except:
            return (
                {'message': 'An error occurred inserting the sale order.'}, 500)
            return (
                sale_order.json(), 201)

    def delete(self, id):
        """
        Finds an item by its name and deletes it.

        :param name: the name of the item.
        :type name: str
        :return: success or failure message.
        :rtype: application/json response.
        """
        sale = SaleModel.find_by_id(id)
        if sale:
            try:
                sale.delete_from_db()
            except:
                return (
                    {'message': 'An error occurred deleting the sale order.'}, 500)
            else:
                return {'message': 'Sale order deleted'}

    def put(self, id):
        """
        Creates or updates an item using the provided name, price and store_id.

        :param id: the id of the sale order.
        :type int

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Sale.parser.parse_args()
        sale = SaleModel.find_by_id(id)
        if sale is None:
            sale_order = Sale_Order(**request_data)
        else:
            sale.date = request_data['date']
            sale.total_price = request_data['total_price']
            sale.payment_type = request_data['payment_type']
            sale.status = request_data['status']
            sale.cust_id = request_data['cust_id']
            try:
                sale.save_to_db()
            except:
                return (
                    {'message': 'An error occurred updating the sale order.'}, 500)
            else:
                return sale.json()


class SaleList(Resource):
    """Stores' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all items.

        :return: all stores' data.
        :rtype: application/json.
        """
        return {'sale': [sale_order.json() for sale_order in SaleModel.query.all()]}