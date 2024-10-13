from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"  # Name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True)  # Primary key
    magnitude = Column(Float)  # To store earthquake magnitude
    location = Column(String)  # To store the earthquake location
    year = Column(Integer)  # To store the year of the earthquake

    def __repr__(self):
        return f"<Earthquake(id={self.id}, magnitude={self.magnitude}, location={self.location}, year={self.year})>"
