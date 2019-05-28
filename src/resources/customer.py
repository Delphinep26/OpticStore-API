from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from src.models.customer import CustomerModel

class Customer(Resource):
    """Customers' endpoint."""
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('last_name',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('birth_date',
                        type=str,
                        required=False,
                        help='Date in the format yyyymmdd')
    parser.add_argument('city',
                        type=str,
                        required=False,
                        help='This field cannot be left blank!')
    parser.add_argument('address',
                        type=str,
                        required=False,
                        help='This field cannot be left blank!')

    @jwt_required
    def get(self, _id):
        """
        Finds an customer by its full name and returns it.

        :param id
        :type id: int
        :return: customer data.
        :rtype: application/json.
        """
        customer = CustomerModel.find_by_id(_id)
        if customer:
            return customer.json()
        else:
            return (
                {'message': 'Customer not found'}, 404)

    def post(self):
        """
        Creates a new customer using the provided first_name, last_name .
        """
        request_data = Customer.parser.parse_args()
        if CustomerModel.find_by_name(request_data['first_name'], request_data['last_name']):
            return (
                {'message': ("An customer with name '{}' '{}' already exists.").format(request_data['first_name'],
                                                                                       request_data['last_name'])}, 400)
        customer = CustomerModel(**request_data)
        try:
            customer.save_to_db()
        except:
            return (
                {'message': 'An error occurred inserting the customer.'}, 500)
        return (
            customer.json(), 201)

    def delete(self, _id):
        """
        Finds an customer by its name and deletes it.

        :param id: the id of the customer.
        :type int
        :return: success or failure message.
        :rtype: application/json response.
        """
        customer = CustomerModel.find_by_id(_id)
        if customer:
            try:
                customer.delete_from_db()
            except:
                return (
                    {'message': 'An error occurred deleting the customer.'}, 500)
            else:
                return {'message': 'Customer deleted'}

    def put(self, _id):
        """
        Creates or updates an customer using the provided name, price and customer_id.

        :param id: the id of the customer.
        :type int:
        :param first_name: the first_name of the customer.
        :type str
        :param last_name: the last_name of the customer.
        :type str

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Customer.parser.parse_args()
        customer = CustomerModel.find_by_id(_id)
        if customer is None:
            customer = CustomerModel(**request_data)
        else:
            customer.first_name = request_data['first_name']
            customer.last_name = request_data['last_name']
            customer.phone = request_data['phone']
            customer.email = request_data['email']
            customer.city = request_data['city']
            customer.address = request_data['address']
            customer.birth_date = request_data['birth_date']
        try:
            customer.save_to_db()
        except:
            return (
                {'message': 'An error occurred updating the customer.'}, 500)
        return customer.json()


class CustomerList(Resource):
    """Customers' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all customers.

        :return: all customers' data.
        :rtype: application/json.
        """
        return {'customers': [customer.json() for customer in CustomerModel.find_all()]}