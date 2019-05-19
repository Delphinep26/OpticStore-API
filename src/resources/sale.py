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
    def get(self, _id):
        """
        Finds an sale by its name and returns it.

        :param id: the id of the sale order.
        :type str
        :return: sale data.
        :rtype: application/json.
        """
        sale_order = SaleModel.find_by_id(_id)
        if sale_order:
            return sale_order.json()
        else:
            return (
                {'message': 'sale order not found'}, 404)

    def post(self):
        """
        Creates a new sale using the provided name, price and sale_id.

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

    def delete(self, _id):
        """
        Finds an sale by its name and deletes it.

        :param name: the name of the sale.
        :type name: str
        :return: success or failure message.
        :rtype: application/json response.
        """
        sale = SaleModel.find_by_id(_id)
        if sale:
            try:
                sale.delete_from_db()
            except:
                return (
                    {'message': 'An error occurred deleting the sale order.'}, 500)
            else:
                return {'message': 'Sale order deleted'}

    def put(self, _id):
        """
        Creates or updates an sale using the provided name, price and sale_id.

        :param id: the id of the sale order.
        :type int

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Sale.parser.parse_args()
        sale = SaleModel.find_by_id(_id)
        if sale is None:
            sale_order = Sale(**request_data)
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
    """Sales' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all sales.

        :return: all sales' data.
        :rtype: application/json.
        """
        return {'sale': [sale_order.json() for sale_order in SaleModel.query.all()]}