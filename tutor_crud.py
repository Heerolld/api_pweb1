from models import db, Tutor

def create_tutor(nome):
    tutor = Tutor(nome=nome)
    db.session.add(tutor)
    db.session.commit()
    return tutor

def get_tutor_by_id(tutor_id):
    return Tutor.query.get(tutor_id)

def get_all_tutors():
    return Tutor.query.all()

def update_tutor(tutor, nome):
    tutor.nome = nome
    db.session.commit()
    return tutor

def delete_tutor(tutor):
    db.session.delete(tutor)
    db.session.commit()
