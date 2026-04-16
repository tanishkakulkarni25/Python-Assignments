#Create a program that takes a filename from the user and tries to open the file for reading and handle these exceptions
#and provide appropriate error messages for following cases.
#1.1) FileNotFoundError: If the file does not exist.
#2.2) PermissionError: If the program lacks permissions to read the file.	
def open_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File contents:", content)

    except FileNotFoundError:
        print("Sorry, File not found. The file does not exist.")
    except PermissionError:
        print("Sorry, could not access the file due to denied permissions.")