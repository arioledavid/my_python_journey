#!/usr/bin/python3
import math
import os
import random
import re
import sys
class Arrays:
    def __init__(self, arrays, length):
        #initialize class
        self.arrays = arrays
        self.length = length

    def reverse(self):
        #print reversed array
        reversed_list = list(reversed(self.arrays))
        print(reversed_list)
        #return (reversed_list)
        for i in range(self.length):
            print(reversed_list[i], end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(arr)

    d = Arrays(arr, n)
    d.reverse()
