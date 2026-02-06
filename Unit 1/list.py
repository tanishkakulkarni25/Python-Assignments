#Write a python program to perform following operations on lists.
#Create and access list elements
days= ["Monday","Tuesday","Wednesday"]
print("List is:",days)
print(days[1])
print(days[-3])

#Add and remove list elements
days.insert(2,"Saturday")
days.append("Sunday")
days.remove("Monday")
print(days)

#Sort list elements
days.sort()
print("Sorted list is :",days)

#Reverse list elements
days.reverse()
print("Reversed list is:",days)