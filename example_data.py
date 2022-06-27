from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_FILENAME = "example.db"
SQLITE_SYNC_URL_PREFIX = "sqlite:///"
NAMES = ["John", "Paul", "George", "Ringo"]

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


def create_example_database():
    sync_disk_engine = create_engine(
        url=SQLITE_SYNC_URL_PREFIX + DB_FILENAME, echo=True
    )
    Base.metadata.create_all(sync_disk_engine)
    sessionmaker_ = sessionmaker(sync_disk_engine)
    with sessionmaker_() as session:
        session.bulk_save_objects([User(name=name) for name in NAMES])
        session.commit()


if __name__ == "__main__":
    create_example_database()
