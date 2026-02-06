#Write a python program to perform following operations on dictionary.
#Create and access elements
my_dictionary= {
    "Name":"Tanishka",
    "Age": 18,
    "City":"Pune"
}
print(my_dictionary)
print(my_dictionary["City"])

#Update
my_dictionary.update([("College","MIT")])
print(my_dictionary)

my_dictionary["Branch"]="CSE"
print(my_dictionary)

#Removing
my_dictionary.pop("Age")
print(my_dictionary)

#Merging dictionaries
dictionary_2= {
    "Class":"SOC 7",
    "ROLL. NO:": 32,
}
print(dictionary_2)
print("Merged dictionaries:",my_dictionary|dictionary_2)