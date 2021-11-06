#!/usr/bin/python3

import math
import os
import random
import re
import sys



class Hourglass:
    def __init__(self, arr):
        #initialize values
        self.arr = arr
        self.m = len(arr) 
        self.n = len(arr[0])

    def hourglassnum(self):
        #algorith to recognize hourglass in array
        count_i = 0
        i = 0
        count_j = 0
        j = 0

        while i < self.m - 2:
            j = count_i
            for x in range(i, i + 3):
                print(f"A[{x}][{j}:{j + 3}]")
            count_i += i
            if count_i == self.m - 3:
                count_i = 0
                i += 1

if __name__ == '__main__':

    #arr = []
    arr = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9],
            [1, 3, 5, 7, 9, 0], [2, 4, 6, 8, 0, 1]]

    #for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))
    d = Hourglass(arr)
    d.hourglassnum()
