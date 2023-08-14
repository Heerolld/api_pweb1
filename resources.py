from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Tutor, Pet, TutorSchema, PetSchema
from tutor_crud import create_tutor, get_tutor_by_id, get_all_tutors, update_tutor, delete_tutor
from pet_crud import create_pet, get_pet_by_id, update_pet, delete_pet

class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutors = get_all_tutors()
            return TutorSchema(many=True).dump(tutors), 200
        
        tutor = get_tutor_by_id(tutor_id)
        return TutorSchema().dump(tutor), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        tutor = create_tutor(args['nome_tutor'])
        return TutorSchema().dump(tutor), 201
 

class PetResource(Resource):
    def get(self, pet_id):
        pet = get_pet_by_id(pet_id)
        return PetSchema().dump(pet), 200

    
