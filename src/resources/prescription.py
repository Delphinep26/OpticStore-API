from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from src.models.prescription import PrescriptionModel

class Prescription(Resource):
    """Prescriptions Order' endpoint."""
    parser = reqparse.RequestParser()
    parser.add_argument('date',
                        type=str,
                        required=False,
                        help='Date in the format yyyymmdd')
    parser.add_argument('sphere_OD',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a sphere_OD.')
    parser.add_argument('sphere_OS',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a sphere_OS.')
    parser.add_argument('cylinder_OD',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a cylinder_OD.')
    parser.add_argument('cylinder_OS',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a cylinder_OS.')
    parser.add_argument('axis_OD',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a axis_OD.')
    parser.add_argument('axis_OS',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a axis_OS.')
    parser.add_argument('pd',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a pd.')
    parser.add_argument('type_name',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a type_name.')
    parser.add_argument('nearsightedness',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a nearsightedness.')
    parser.add_argument('farsightedness',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a farsightedness.')
    parser.add_argument('document_id',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a document_id.')
    parser.add_argument('customer_id',
                        type=str,
                        required=True,
                        help='Every prescriptions needs a customer_id.')
    @jwt_required
    def get(self, _id):
        """
        Finds an Prescription by its name and returns it.

        :param id: the id of the Prescription order.
        :type str
        :return: Prescription data.
        :rtype: application/json.
        """
        prescription = PrescriptionModel.find_by_id(_id)
        if prescription:
            return prescription.json()
        else:
            return (
                {'message': 'Prescription order not found'}, 404)

    def post(self):
        """
        Creates a new Prescription using the provided name, price and Prescription_id.

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Prescription.parser.parse_args()
        print(request_data)
        prescription = PrescriptionModel(**request_data)
        #try:
        prescription.save_to_db()
        #except:
         #   return (
          #      {'message': 'An error occurred inserting the Prescription.'}, 500)
        return (
            prescription.json(), 201)

    def delete(self, _id):
        """
        Finds an Prescription by its name and deletes it.

        :param name: the name of the Prescription.
        :type name: str
        :return: success or failure message.
        :rtype: application/json response.
        """
        prescription = PrescriptionModel.find_by_id(_id)
        if prescription:
            try:
                prescription.delete_from_db()
                return {'message': 'Prescription order deleted'}
            except:
                return (
                    {'message': 'An error occurred deleting the Prescription order.'}, 500)
        else:
            return {'message': 'Prescription Not Found'}


    def put(self, _id):
        """
        Creates or updates an Prescription using the provided name, price and Prescription_id.

        :param id: the id of the Prescription order.
        :type int

        :return: success or failure message.
        :rtype: application/json response.
        """
        request_data = Prescription.parser.parse_args()
        prescription = PrescriptionModel(**request_data)
        if prescription is None:
            prescription = PrescriptionModel(**request_data)
        else:
            prescription.date = request_data['date']

            try:
                prescription.save_to_db()
            except:
                return (
                    {'message': 'An error occurred updating the Prescription order.'}, 500)
            else:
                return prescription.json()


class PrescriptionList(Resource):
    """Prescriptions' list endpoint."""

    @classmethod
    def get(cls):
        """
        Returns a list of all Prescriptions.

        :return: all Prescriptions' data.
        :rtype: application/json.
        """
        return {'Prescription': [prescription.json() for prescription in PrescriptionModel.find_all()]}