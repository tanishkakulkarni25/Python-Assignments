#Write a program to demonstarte fundamental file handling options like opening a file, reading its contents,
#writing data to it, appending additional content, and ensuring proper closing of the file.
with open("data.txt","w") as file:
    file.write("This is Tanishka Kulkarni.\n")
    file.write("I'm trying file handling in Python.")
file.close()

with open("data.txt","a") as file:
    file.write("Thank you")
file.close()

with open("data.txt","r") as file:
    content= file.read()
    print("File contents are:",content)
file.close()
