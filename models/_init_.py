#!/usr/bin/python3
"""
Initialize the 'models' directory with the '__init__' magic method.
This script imports the 'FileStorage' class from the 'models.engine.file_storage' module, creates an instance of it, and then reloads it.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
