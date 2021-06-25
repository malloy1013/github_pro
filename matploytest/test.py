import sys
import os
import glob
# root = os.getcwd()
# for a,b,c in os.walk(root,topdown=True):
#     print(a)
#     print(b)
#     print(c)

# print(os.path.abspath('.'))
if __name__ == '__main__':
    print(glob.glob('.idea/*'))