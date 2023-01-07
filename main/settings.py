import os
from pathlib import Path
from models import JsonDB, CSVDB

BASE_DIR = os.getcwd()

SECRET_KEY = "kgbnexyqyotiwczjrgkjsadotnkexzxkqgb"

# We can choose between JsonDB or CsvDB
# It all comes with the user preference on what he will going to use the data
DATABASE_FILE_PATH = Path(BASE_DIR, "data.json")
DATABASE = JsonDB(DATABASE_FILE_PATH)
