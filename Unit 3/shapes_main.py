#Create a module called shapes.py with functions to calculate the area of a circle, and rectangle and triangle.
#Based on the user input, determine and show the areas of shapes using user module.
import shapes

print("Choose a shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius of circle: "))
    print("Area of Circle:", shapes.area_circle(r))

elif choice == 2:
    l = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    print("Area of Rectangle:", shapes.area_rectangle(l, w))

elif choice == 3:
    b = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    print("Area of Triangle:", shapes.area_triangle(b, h))

else:
    print("Invalid choice!")