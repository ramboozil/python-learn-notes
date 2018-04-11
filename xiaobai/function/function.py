import math


def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    return str(fahrenheit) + '˚F'


C2F = fahrenheit_converter(35)
print(C2F)


def g2kg(m):
    km = m / 1000
    return str(km) + 'kg'


v = g2kg(1024)
print(v)


def gougu(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c


print(gougu(3, 4))


def transform(a, b):
    return 'The right triangle third side\'s length is {}'.format((a ** 2 + b ** 2) ** (1 / 2))


print(transform(3, 4))


def trapezoid_area(base_up, base_down, height):
    return 1 / 2 * (base_up + base_down) * height


print(trapezoid_area(1, 2, 3))


print('   *', '  * *', ' * * *', '   |   ', sep='\n')
