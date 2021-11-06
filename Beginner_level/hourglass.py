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
        self.arry = []

    def hourglassnum(self):
        #algorith to recognize hourglass in array
        count_i = 0
        i = 0
        count_j = 0
        j = 0

        while i < self.m - 2:
            while count_i < self.m - 2:
                j = count_i
                for x in range(i, i + 3):
                    self.arry.append(self.arr[x][j:j+3])
                    count_j += 1
                count_i += 1
            count_i = 0
            i += 1

    def glass_sum(self):
        #add the hourglass and compare sums for the largest
        z = len(self.arry)
        sum_arry = float('-inf')
        for i in range(0, z, 3):
            sum_temp = sum(self.arry[i]) + self.arry[i + 1][1] + sum(self.arry[i + 2])
            print(sum_temp)
            if sum_temp > sum_arry:
                sum_arry = sum_temp
            print(sum_arry)
        print(sum_arry)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    d = Hourglass(arr)
    d.hourglassnum()
    d.glass_sum()
