
from math import *
r = 3840*2160
i = 24
k = 0
for x in range(1,100000):
    if x * r * i < 32*1024*1024*1024*8:
        k += 1

print(ceil(13269234531/k))
