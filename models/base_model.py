#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)

        created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
        )

        updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow()
        )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())  # Always generate a new ID
        self.created_at = self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            setattr(self, key, value)  # Use setattr to set attributes

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()  # Update updated_at with current time
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update({
            '__class__': type(self).__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
