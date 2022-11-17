from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, TEXT, DATE
from sqlalchemy import insert

DATABASE_NAME = 'test_task_db.sqlite'
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
metadata = MetaData()


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50))


class Users(Base):
    __tablename__ = 'users'
    id = Column(BIGINT, primary_key=True)
    fio = Column(TEXT)
    datar = Column(DATE)
    id_role = (Integer, ForeignKey('roles.id'))


Base.metadata.create_all(engine)
