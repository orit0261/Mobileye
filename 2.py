# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

num=1

len1=math.floor(math.log(num, 10)) + 1

len1=len1-1
if len1==0:
    num_f=0
else:
    num_f=10**len1
print(num_f)

