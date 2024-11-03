# ANSWER # 01

a=6
b=2
c=2
n=3
print(a+b+c)       # SUM
print(a-b-c)       # DIFFERNCE
print((a+b+c)/n)   # AVERAGE
# ANSWER # 02

# AREA OF TRIANGLE
a = int(input("enter the length of first side"))
b = int(input("enter the length of second side"))
c = int(input("enter the length of third side"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle is:",area)

# AREA OF CIRCLE
radius = float(input("enter theradius of the circle"))
area = 3.14*radius*radius
print("area of circle is:",area)

# AREA OF SQURE
side=int(input("enter side: "))
area=side*side
print("area of square: ",area)

#  AREA OF RECTANGLE
l=int(input('enter heigth: '))
b=int(input('enter length '))
area=l*b
print("area of rectangle: ",area)