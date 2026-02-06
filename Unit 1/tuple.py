#Write a python program to perform the following operations on tuples.
#Create and access tuples
my_tuple= ("Engineering","Architecture","Design","Finance","Music")
print("Fields:",my_tuple)
print(my_tuple[0])
print(my_tuple[-4])

#Nested tuple
my_tuple= ("Engineering",("Computer science","Aerospace","Mechanical"),"Architecture","Design","Finance","Music")
print(my_tuple)

#Repetition
print(my_tuple * 2)

#Concatenation of tuples
tuple_2= ("MIT","Cambridge","Harvard","Oxford","Melbourne University")
print(tuple_2)
concate= my_tuple + tuple_2
print(concate)