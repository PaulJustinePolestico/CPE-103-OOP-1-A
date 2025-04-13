import os

def create_file():
    with open("SURNAME.txt", "w") as fhand:
        fhand.write("Welcome.This is my analysis.\n")
    print("File created successfully!")

def read_file():
    try:
        with open("SURNAME.txt", "r") as fhand:
            content = fhand.read()
            print("File Contents: \n",content)
    except FileNotFoundError:
        print("Error: File Not Found!")


def update_file():
     with open("SURNAME.txt", "a") as fhand:
         fhand.write("Adding a new to this file!\n")
     print("File updated successfully!")

def delete_file():
    if os.path.exists("SURNAME.txt"):
        os.remove("SURNAME.txt")
        print("File deleted successfully!")
    else:
        print("Error: File not found!")

create_file()
read_file()
update_file()
read_file()
delete_file()
