from sqlalchemy import create_engine, and_, select, table, column
from models import Dog
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
t = table("dogs", column("id"), column("name"), column("breed"))

def create_table(base):
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    with session.begin():
        session.add(dog)
    return session

def new_from_db(session):
    return session.query(Dog).first()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    # return session.query(Dog).filter_by(name=name).first()
    query = select(Dog).where(Dog.name==name)
    return session.scalars(query).first()

def find_by_id(session, id):
    return session.get(Dog, id)

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(
        Dog.name == name, 
        Dog.breed == breed
    ).first()
    # query = select(Dog).where(
    #     and_(
    #         Dog.name==name,
    #         Dog.breed==breed
    #     )
    # )
    # return session.scalars(query).first()

def update_breed(session, dog, breed):
    # session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})
    dog.breed = breed
    session.commit()
    return session