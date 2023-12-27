from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, JSON
from enum import Enum
from uuid import uuid4


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: uuid4().hex)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    gender = Column(String)


# class Customer(Base):
#     __tablename__ = "customers"
#
#     id = Column(String, primary_key=True, default=lambda: uuid4().hex)
#     name = Column(String)
#     org_id = Column(Integer)
#     user_id = Column(String, ForeignKey("users.id"))
#     user = relationship("User", lazy="selectin")
#
#
# class Supplier(Base):
#     __tablename__ = "suppliers"
#
#     id = Column(String, primary_key=True, default=lambda: uuid4().hex)
#     name = Column(String)
#     org_id = Column(Integer)
#     user_id = Column(String, ForeignKey("users.id"))
#     user = relationship("User", lazy="selectin")
#
#
# class Invoice(Base):
#     __tablename__ = "invoices"
#
#     id = Column(String, primary_key=True, default=lambda: uuid4().hex)
#     customer_id = Column(String, ForeignKey("customers.id"))
#     supplier_id = Column(String, ForeignKey("suppliers.id"))
#     date = Column(DateTime)
#     data = Column(JSON)
