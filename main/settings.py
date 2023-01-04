import os
from pathlib import Path
from models import JsonDB, CSVDB

BASE_DIR = os.getcwd()


# We can choose between JsonFile or CsvFile
DATABASE_FILE_PATH = Path(BASE_DIR, "data")
DATABASE = CSVDB(DATABASE_FILE_PATH)
