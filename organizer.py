import os
import datetime

FOLDER_PATH = "C:\\Users\\N_Has\OneDrive\\Pictures\\Screenshots"

for file_path in os.listdir(FOLDER_PATH):
    if not file_path.startswith(".") and not file_path.lower() == "desktop.ini":
        creation_time = os.path.getctime(FOLDER_PATH + '\\' + file_path)
        timestamp = datetime.datetime.fromtimestamp(creation_time)
        print(timestamp)