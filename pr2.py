import math
x = 2.735
z = 7.218
x_radian = math.radians(x)
print(((z + x) / math.cos(x_radian) + (math.sin(x_radian) * math.cos(x_radian)) ** 0.5) + 16 * z) 