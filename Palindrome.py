class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_palindrome(word):

    stack = Stack()
    queue = Queue()

    for char in word.lower():
        stack.push(char)
        queue.enqueue(char)

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            print(f"The word '{word}' is a not palindrome")
            return False


    print(f"The word '{word}' is a palindrome")
    return True


if __name__ == "__main__":
    print("Enter a string to check if its a palindrome:")
    s = input()

    is_palindrome(s)