#Write a program to convert a JSON array into a csv file.
import json
import csv

with open("data.json") as file:
    data = json.load(file)
file.close()

with open("output.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
file.close()
print(data)