#Write a python prgram to perform the following operations on set.
#Create and access set elements.
set1= {"2","8","1","9","20","24"}
set2= {"3","2","9","25","15","30","20"}
print("Set 1 is:",set1)
print("Set 2 is:",set2)

#Union
print("Union of two sets is:",set1.union(set2))

#Intersection
print("Intersection of two sets is:",set1.intersection(set2))

#Difference
print("Difference is:",set1.difference(set2))
print("Difference is:",set2.difference(set1))

#Symmetric difference
print("Symmetric difference is:",set1.symmetric_difference(set2))