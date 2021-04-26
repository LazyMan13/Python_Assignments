#pi's simple constant
pi = 3.14
#radius of circle
circleRadius = 4
#rectangle's height
rectangleH = 2
#rectangle's width
rectangleW = 3
#rectangle's length
rectangleL = 5
#triangle's side A
triangleA = 3
#triangle's side B
triangleB = 3
#triangle's side C
triangleC = 2

#Circe Area = pi(3.14) times the radius squared
circleArea = pi * circleRadius * circleRadius
#Rectangular Volume = Height times Length times Width
rectangleVol = rectangleH * rectangleL * rectangleW
#Triangle Perimeter  = SideA plus SideB plus SideC
trianglePerimeter = triangleA + triangleB + triangleC

print(f"The Area of a Circle with a radius of {circleRadius} is {circleArea}.")
print(f"The Volume of a Rectangular Prism with dimensions of {rectangleH}, {rectangleL}, and {rectangleW} is {rectangleVol}.")
print(f"The Perimeter of a Triangle with sides {triangleA}, {triangleB}, and {triangleC} is {trianglePerimeter}.")
