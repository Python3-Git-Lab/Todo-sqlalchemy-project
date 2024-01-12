# models.py
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///todo.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

    #rlshp
    tasks= relationship("Task", backref=backref("user"), cascade='all, delete-orphan')

    def _repr__(self):
        return f"Username: {self.username}"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    #rlshp
    task_id= Column(Integer(), ForeignKey('tasks.id'))

    def __repr__(self):
        return f"Category name: {self.name}"

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)

    #Rlshp
    user_id = Column(Integer, ForeignKey('users.id'))
    
    categories= relationship("Category", backref=backref('task'), cascade= "all, delete-orphan")

    def __repr__(self):
        return f"Title: {self.title} Status: {self.status}"
