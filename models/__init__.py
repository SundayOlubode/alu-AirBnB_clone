#!/usr/bin/python3
# from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.engine import file_storage
from models.base_model import BaseModel

storage = file_storage.FileStorage()
storage.reload()
