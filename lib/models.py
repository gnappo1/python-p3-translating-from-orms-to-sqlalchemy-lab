#!/usr/bin/env python3
import os
# os.environ["SQLALCHEMY_SILENCE_UBER_WARNING"] = "1"
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'
        ),
    )

    id = Column(Integer())
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"Dog {self.id}: {self.name}" \
            + f"Breed: {self.breed}"

if __name__ == "__main__":
    import ipdb; ipdb.set_trace()
