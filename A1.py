
"""Lab Assignment 1

Consider telephone book database of N clients.
Make use of a hash table implementation to quickly look up client‘s telephone number.
Make use of two collision handling techniques and compare them 
using number of comparisons required to find a set of telephone numbers"""



import hashlib

class Node:
    def __init__(self):
        self.name = ""
        self.telephone = ""
        self.key = 0

class Hashing:
    def __init__(self):
        self.data = [Node() for _ in range(100)]  # Size of directory -> 100
        self.size = 100
        self.k = 0

    def ascii_generator(self, s):
        return sum(ord(c) for c in s) % 100

    def create_record(self, n, tele):
        k = self.ascii_generator(n)
        index = k % self.size
        for _ in range(self.size):
            if self.data[index].key == 0:
                self.data[index].key = k
                self.data[index].name = n
                self.data[index].telephone = tele
                break
            else:
                index = (index + 1) % self.size

    def search_record(self, name):
        k = self.ascii_generator(name)
        index = k % self.size
        for _ in range(self.size):
            if self.data[index].key == k:
                print("\nRecord found")
                print("Name :: ", self.data[index].name)
                print("Telephone :: ", self.data[index].telephone)
                return
            else:
                index = (index + 1) % self.size
        print("Record not found")

    def delete_record(self, name):
        key = self.ascii_generator(name)
        index = key % self.size
        for _ in range(self.size):
            if self.data[index].key == key:
                self.data[index].key = 0
                self.data[index].name = ""
                self.data[index].telephone = ""
                print("\nRecord Deleted successfully")
                return
            else:
                index = (index + 1) % self.size
        print("\nRecord not found")

    def update_record(self, name):
        key = self.ascii_generator(name)
        index = key % self.size
        for _ in range(self.size):
            if self.data[index].key == key:
                new_telephone = input("Enter the new telephone number :: ")
                self.data[index].telephone = new_telephone
                print("\nRecord Updated successfully")
                return
            else:
                index = (index + 1) % self.size
        print("\nRecord not found")

    def display_record(self):
        print("\t  Name  \t\t Telephone")
        for node in self.data:
            if node.key != 0:
                print(f"\t{node.name} \t\t\t {node.telephone}")

def main():
    s = Hashing()
    loop = True
    while loop:
        print("\n-------------------------")
        print(" Telephone book Database ")
        print("-------------------------")
        print("1. Create Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Display Directory")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name: ")
            telephone = input("Enter the telephone number: ")
            s.create_record(name, telephone)
        elif choice == 2:
            name = input("Enter the name to search: ")
            s.search_record(name)
        elif choice == 3:
            name = input("Enter the name to delete: ")
            s.delete_record(name)
        elif choice == 4:
            name = input("Enter the name to update: ")
            s.update_record(name)
        elif choice == 5:
            s.display_record()
        elif choice == 6:
            loop = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

