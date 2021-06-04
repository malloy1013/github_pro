import sys
import os
root = os.getcwd()
for a,b,c in os.walk(root,topdown=True):
    print(a)
    print(b)
    print(c)

# print(os.path.abspath('.'))