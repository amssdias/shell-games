from models import FileDB, JsonFile

# We can choose between JsonFile or CsvFile
DATABASE = FileDB(file_type=JsonFile(), file_path="data.json")