import os
import datetime
#use glob to filter files later
import tkinter as tk
from tkinter import messagebox
import shutil

FOLDER_PATH = r'C:\Users\N_Has\OneDrive\Pictures\Screenshots'

def get_unique_filename(folder, filename):
    """Ensure unique filenames by adding a counter if needed."""
    base, ext = os.path.splitext(filename)  # Get name and extension
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{base}({counter}){ext}"  # Append a counter
        counter += 1

    return new_filename


root = tk.Tk()
root.withdraw()  # Hide the main window (since we only want the pop-up)

#TODO: split renaming and reorganization into separate functions and give user the option
for file_name in os.listdir(FOLDER_PATH):
    if not file_name.startswith(".") and not file_name.lower() == "desktop.ini":
        path = os.path.join(FOLDER_PATH, file_name)
        file_extension = '.png'

        creation_time = os.path.getctime(path)
        timestamp = datetime.datetime.fromtimestamp(creation_time)
    
        # Convert timestamp to string for file name
        timestamp_str = timestamp.strftime("%d-%m-%Y %H-%M")

        #resetting file name
        reset_name = f'lol{file_extension}'
        reset_name_path = os.path.join(FOLDER_PATH, reset_name)
        os.rename(path, reset_name_path)

        #renaming
        file_name = get_unique_filename(FOLDER_PATH, f"{timestamp_str}{file_extension}")
        new_path = os.path.join(FOLDER_PATH, file_name)
        os.rename(reset_name_path, new_path)

        #destination folder
        destination_folder_year = FOLDER_PATH + '\\' + timestamp.strftime("%Y") 
        os.makedirs(destination_folder_year, exist_ok=True)

        destination_folder_month = destination_folder_year + '\\' + timestamp.strftime("%B")
        os.makedirs(destination_folder_month, exist_ok=True)

        #moving the image
        shutil.move(new_path, destination_folder_month)


messagebox.showinfo("Information", "The files in this folder have been renamed sucessfully!")
