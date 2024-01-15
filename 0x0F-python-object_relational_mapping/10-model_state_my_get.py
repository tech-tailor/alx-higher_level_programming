#!/usr/bin/python3
"""
list all objects from the database
"""


from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_items = session.query(State).filter(State.name == sys.argv[4]).all()
    if not all_items:
        print("Not found")
    else:
        for item in all_items:
            print(f"{item.id}")

    session.close()
