from math import *

x = 6.251
y = 0.827
z = 25.001
d = cos(y)**3
c = abs(x-y)*(1+((sin(z)**2)/sqrt(x+y)))
w = exp(abs(x-y)) + (x/2)
s = y**cbrt(abs(x))+d*(c/w)

print(s)
