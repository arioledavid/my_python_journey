class Difference():
    def __init__(self,a):
        self.maximumDifference = 0
        self.__elements = a

    def computeDifference(self):
        length = len(self.__elements)
        arr = self.__elements
        result = 0
        for i in range(length):
            j = i + 1
            for j in range(j, length):
                result = abs(arr[i] - arr[j])
                if result > self.maximumDifference:
                    self.maximumDifference = result

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
