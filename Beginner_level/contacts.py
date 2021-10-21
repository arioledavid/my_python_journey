#!/usr/bin/python3

class Contacts:
    def __init__(self, key, value):
        #initialize values from input
        self.key = key
        self.value = value

    def addContact(self):
        #Add Contact to dictionary
        add = dict(zip(self.key, self.value))
        return add

    def searchContact(self, add, name):
        #Search through contact
        if name in add:
            print(f"{name}={add[name]}")
        else:
            print("Not found")
        
t = int(input())
keys = []
values = []
#take input for number of t times 
for i in range(t):
    key,value = input().split()
    keys.append(key)
    values.append(value)
c = Contacts(keys, values)
contacts = c.addContact()

inp = input()
while inp != "":
    c.searchContact(contacts, inp)
    try:
        inp = input()
    except EOFError:
        quit()
