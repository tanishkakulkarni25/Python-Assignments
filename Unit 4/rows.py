#Write a python program to count the total no. of rows in a csv file.
import csv
filename = "sample.csv"  
try:
    with open(filename, "r") as file:
        reader = csv.reader(file)
        row_count= 0
        for row in reader:
            row_count+=1
    print("Total number of rows in",filename,":",row_count)

except FileNotFoundError:
    print("File not found. Sorry.")