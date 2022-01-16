from sqlalchemy.orm import Session

from . import models, schemas


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(
        name=pet.name, animal=pet.animal, gender=pet.gender, born=pet.born
    )
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def update_pet(db: Session, pet_id: int, pet: schemas.PetCreate):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db_pet.name = pet.name
    db_pet.animal = pet.animal
    db_pet.gender = pet.gender
    db_pet.born = pet.born
    db.commit()
    db.refresh(db_pet)
    return db_pet


def delete_pet(db: Session, pet_id: schemas.PetCreate):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db.delete(db_pet)
    db.commit()
