# Function to calculate the area of a circle

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))

print("Area of the circle:", area_of_circle(radius))