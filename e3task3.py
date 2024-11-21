import numpy as np
import math

#strecke 300
#radius 55,54
s = 300
d = 55.54

r = d/2
u =(math.pi*d)

n360 = s//u

rest_s= s - n360 * u
rest_winkel = 360*(rest_s / u)


run_angel = 360 * n360 + rest_winkel

print(u)
print(n360)
print(rest_s)
print(rest_winkel)
print(run_angel)
