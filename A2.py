"""Implement all the functions of a dictionary (ADT) using hashing and handle collisions
using chaining with / without replacement.
Data: Set of (key, value) pairs, Keys are mapped to values, Keys must be comparable, Keys
must be unique
Standard Operations: Insert(key, value), Find(key), Delete(key)"""
import sys

class Data:
    def __init__(self):
        self.name = ""
        self.name1 = ""

class Hash:
    def __init__(self):
        self.n = 0
        self.sum = 0
        self.x = 0
        self.c = 0
        self.i = 0
        self.j = 0
        self.d = [Data() for _ in range(10)]

    def insert(self):
        print("\n enter no. of words")
        self.n = int(input())
        for self.j in range(self.n):
            print("\n\n enter the word")
            self.na = input()
            print("\n enter the meaning of that word")
            self.na1 = input()
            self.sum = 0
            for self.i in range(len(self.na)):
                self.sum += ord(self.na[self.i])
            self.x = (self.sum // len(self.na)) % 10
            print(self.x)
            self.c = self.x
            while True:
                if self.d[self.x].name == "":
                    self.d[self.x].name = self.na
                    self.d[self.x].name1 = self.na1
                    break
                self.x = (self.x + 1) % 10
                if self.c == self.x:
                    print("\n hash table is full")
                    break

    def search(self):
        print("\n enter the word whose meaning you want")
        self.na = input()
        self.sum = 0
        for self.i in range(len(self.na)):
            self.sum += ord(self.na[self.i])
        self.x = (self.sum // len(self.na)) % 10
        self.c = self.x
        while True:
            if self.d[self.x].name == self.na:
                print("\n MEANING-> " + self.d[self.x].name + "=" + self.d[self.x].name1)
                break
            self.x = (self.x + 1) % 10
            if self.c == self.x:
                print("\n word not found")
                break

    def delete(self):
        print("\n enter the word which is to be deleted")
        self.na = input()
        self.sum = 0
        for self.i in range(len(self.na)):
            self.sum += ord(self.na[self.i])
        self.x = (self.sum // len(self.na)) % 10
        self.c = self.x
        while True:
            if self.d[self.x].name == self.na:
                print("\n" + self.d[self.x].name + " word deleted")
                self.d[self.x].name = ""
                self.d[self.x].name1 = ""
                break
            self.x = (self.x + 1) % 10
            if self.c == self.x:
                print("\n word not found")
                break

    def display(self):
        for i in range(10):
            print(f"\n{self.d[i].name} {self.d[i].name1}")

def main():
    h = Hash()
    while True:
        print("\n enter the choice")
        print("\n 1.insert word and its meaning")
        print("\n 2.find meaning")
        print("\n 3.delete the word")
        print("\n 4.exit")
        n = int(input())
        if n == 1:
            h.insert()
        elif n == 2:
            h.search()
        elif n == 3:
            h.delete()
        elif n == 4:
            sys.exit(0)
        else:
            print("\n unknown choice")

if __name__ == "__main__":
    main()

