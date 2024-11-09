# arrays.py

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = [fill_value] * capacity

    def __str__(self):
        return str(self.items)
    
    def insert(self, index, value):
        if 0 <= index <= len(self.items):
            self.items = self.items[:index] + [value] + self.items[index:]
        else:
            print(f"Error: Index {index} is out of bounds")

    def delete(self, index):
        if 0 <= index < len(self.items):
            self.items = self.items[:index] + self.items[index+1:]
        else:
            print(f"Error: Index {index} is out of bounds")


# Testing the Array class with insert and delete
if __name__ == "__main__":
    arr = Array(5, 0)
    print(arr)  # [0, 0, 0, 0, 0]

    arr.insert(2, 10)
    print(arr)  # [0, 0, 10, 0, 0, 0]

    arr.insert(4, 20)
    print(arr)  # [0, 0, 10, 0, 20, 0, 0]

    arr.delete(3)
    print(arr)  # [0, 0, 10, 20, 0, 0]

    arr.insert(10, 30)  # Error: Index out of bounds
    arr.delete(10)  # Error: Index out of bounds

