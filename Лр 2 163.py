import math
type_of_figure = input("triangle, circle or rectangle(lowercase only):")
if type_of_figure == 'triangle':
    a = float(input("Enter a size of side a:"))
    b = float(input("Enter a size of side b:"))
    c = float(input("Enter a size of side c:"))
    p = (a + b + c) / 2
    print("result:", math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif type_of_figure == 'circle':
    r = float(input("Radius:"))
    print("result:", math.pi * (r ** 2))
elif type_of_figure == 'rectangle':
    s1 = float(input("first side:"))
    s2 = float(input("second side:"))
    print("result", s1 * s2)
else:
    print("no detection")
