from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from src.models.sale import SaleModel

class Sale(Resource):
    """sales' endpoint."""
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
    parser.add_argument('customer_id',
                        type=str,
                        required=True,
                        help='Every sales needs a customer_id.')

    @jwt_required
    def get(self, _id):
        """
        Finds an sale by its name and returns it.

        :param id: the id of the sale.
        :type str
        :return: sale data.
        :rtype: application/json.
        """
        sale = SaleModel.find_by_id(_id)
        if sale:
            return sale.json()
        else:
            return (
                {'message': 'sale  not found'}, 404)

    def post(self):
        """
        Creates a new sale using the provided name, price and sale_id.

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Sale.parser.parse_args()
        sale = SaleModel(**request_data)
        try:
            sale.save_to_db()
        except:
            return (
                {'message': 'An error occurred inserting the sale .'}, 500)
        return (
            sale.json(), 201)

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
                    {'message': 'An error occurred deleting the sale .'}, 500)
            else:
                return {'message': 'sale  deleted'}

    def put(self, _id):
        """
        Creates or updates an sale using the provided name, price and sale_id.

        :param id: the id of the sale .
        :type int

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Sale.parser.parse_args()
        sale = SaleModel.find_by_id(_id)
        if sale is None:
            sale = sale(**request_data)
        else:
            sale.date = request_data['date']
            sale.total_price = request_data['total_price']
            sale.payment_type = request_data['payment_type']
            sale.status = request_data['status']
            sale.customer_id = request_data['customer_id']
            try:
                sale.save_to_db()
            except:
                return (
                    {'message': 'An error occurred updating the sale .'}, 500)
            else:
                return sale.json()


class SaleList(Resource):
    """sales' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all sales.

        :return: all sales' data.
        :rtype: application/json.
        """
        return {'sale': [sale.json() for sale in SaleModel.find_all()]}