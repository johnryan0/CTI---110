"""
(Block comments -- continue until the triple quotes end )
CTI 110
P2LAB1
Bardaji
9/15/26
Get radius, calculate and display radius, circumference, and area 
"""
PI = 3.14159
# Input to get raidus 
radius = float(input("What is the raidus of the circle? "))


# Calculation -- find diameter, circumference, and area
# Diameter = 2r, circumference = 2pir, area = pi*r*r
diameter = 2 * radius 
circumference = 2 * PI * radius 
area = PI * radius * radius 

# output
print(f"The diameter is {diameter:.1f}.")
print(f"The circumference is {circumference:.2f}")
print(f"the area is {area:.3f}")