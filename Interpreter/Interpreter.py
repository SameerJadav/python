expression = input("expression: ")

#.split() will split one string into diffrent variables
#you need to state the point from where you want to split the string
x, y, z = expression.split(" ")

#changing the vale of variables to floating values
_x = float(x)
_z = float(z)

if y == "+":
    result = _x + _z
if y == "-":
    result = _x - _z
if y == "*":
    result = _x * _z
if y == "/":
    result = _x / _z
print(round(result, 1))