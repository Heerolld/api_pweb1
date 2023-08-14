from models import db, Pet

def create_pet(nome, tutor_id):
    pet = Pet(nome=nome, tutor_id=tutor_id)
    db.session.add(pet)
    db.session.commit()
    return pet

def get_pet_by_id(pet_id):
    return Pet.query.get(pet_id)

def update_pet(pet, nome, tutor_id):
    pet.nome = nome
    pet.tutor_id = tutor_id
    db.session.commit()
    return pet

def delete_pet(pet):
    db.session.delete(pet)
    db.session.commit()
