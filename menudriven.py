#menu driven program to calculate area and perimeter of differnet shapes
#user defined functions start
#Declaring all the required functions with the calculations of area of different shapes
def area_circle(radius):
    area = 3.14 * radius * radius
    print("Area of Circle: ", area)

def area_triangle(base, height):
    area = base * height / 2
    print("Area of Triangle: ", area)

def area_rectangle(height, width):
    area = height * width
    print("Area of Rectangle: ", area)

def area_square(side):
    area = side * side
    print("Area of Square: ", area)

#Declaring all the required functions with the calculations of perimater of different shapes
def perimeter_circle(radius):
    perimeter = 2 * 3.14 * radius
    print("Perimeter of Circle: ", perimeter)

def perimeter_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    print("Perimeter of Triangle: ", perimeter)

def perimeter_rectangle(height, width):
    perimeter = 2 * (height + width)
    print("Perimeter of Rectangle: ", perimeter)

def perimeter_square(side):
    perimeter = 4 * side
    print("Perimeter of Square: ", perimeter)

#user defined function ends
print("\nWELCOME!!")
print("HERE YOU CAN CALCULATE AREA AND PERIMETER OF DIFFERENT SHAPES!")

print("\nMENU")
print("1. Circle")
print("2. Triangle")
print("3. Rectangle")
print("4. Square")
print("5. Exit")
while True:
    shape_choice = int(input("\nEnter your choice of shape for calculations: "))
    
    if shape_choice == 1:
        radius = float(input("Enter Radius of Circle: "))
        perimeter_circle(radius)
        area_circle(radius)
    
    elif shape_choice == 2:
        side1 = float(input("Enter length of side1: "))
        side2 = float(input("Enter length of side2: "))
        side3 = float(input("Enter length of side3: "))
        perimeter_triangle(side1,side2,side3)
        print("")
        base = float(input("Enter base of traingle: "))
        height = float(input("Enter height of traingle: "))
        area_triangle(base, height)

    elif shape_choice == 3:
        height = float(input("Enter height of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        perimeter_rectangle(height,width)
        area_rectangle(height,width)
        
    elif shape_choice == 4:
        side = float(input("Enter side of square: "))
        perimeter_square(side)
        area_square(side)
           
    elif shape_choice == 5:
        print("Thank You! See you again.")
        break

    else:
        print("Incorrect Choice. Please, try again.")
