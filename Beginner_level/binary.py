#!/usr/bin/python3

import math
import os
import random
import re
import sys

class Binary:
    def __init__(self, num):
        #initialize class 
        self.num = num

    def convert(self):
        #covert int decimal input to binary
        n = self.num
        binary = []
       
        while n > 0:
            rem = n % 2
            quotient = int(n / 2)
            if n != 1:
                binary.append(rem)
                n = quotient
            elif n == 1:
                binary.append(1)
                n = 0
        binary = list(reversed(binary))
        return binary

    def count(self, binary):
        count = 0
        temp = 0
        
        for i in binary:
            if i == 1:
                temp += 1
                if temp >= count:
                    count = temp
            elif i == 0:
                temp = 0

        print(count)


if __name__ == '__main__':
    n = int(input().strip())
    d = Binary(n)
    listnum = d.convert()
    d.count(listnum)
