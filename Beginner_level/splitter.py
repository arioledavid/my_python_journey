class Splitter:
    def __init__(self, string):
        self.string = string
        self.length = len(string)

    def split(self):
        str_even = string[0:self.length:2]
        str_odd = string[1:self.length:2]
        print(f"{str_even} {str_odd}")
t = int(input())
for i in range(0, t):
    string = str(input())
    p = Splitter(string)
    p.split()
