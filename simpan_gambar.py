import mysql.connector
import cv2
import tkinter as tk
from tkinter import filedialog

# Function to open file dialog and select image
def open_file_dialog():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    return img

# Function to save image to MySQL database
def save_to_database(img_data, name):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="opencv"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO dataset (nama, foto) VALUES (%s, %s)"
    val = (name, img_data)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    data_label=tk.Label(window,text="data berhasil di tambah")
    data_label.pack()

# Function to handle button click and save image to database
def handle_save_button():
    img = open_file_dialog()
    img_data = cv2.imencode('.jpg', img)[1].tobytes()
    name = name_entry.get()
    save_to_database(img_data, name)
    name_entry.delete(0,'end')

# Create GUI window
window = tk.Tk()

# Create name entry field
name_label = tk.Label(window, text="Nama")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Create save button
save_button = tk.Button(window, text="Save", command=handle_save_button)
save_button.pack()

# Run GUI window
window.mainloop()
