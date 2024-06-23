class Stack:
    __stack = []

    def __init__(self, capacity):
        self.__capacity = capacity

    def is_empty(self):
        if (len(self.__stack) == 0):
            return True
        return False

    def is_full(self):
        if (len(self.__stack) >= self.__capacity):
            return True
        return False

    def pop(self):
        if (self.is_empty()):
            print("Stack is empty")
            return
        return self.__stack.pop()

    def push(self, value):
        if (self.is_full()):
            print("Stack is full")
            return
        self.__stack.append(value)

    def top(self):
        return self.__stack[-1]

    def describe(self):
        print(self.__stack)


stack1 = Stack(5)
stack1.push(1)
stack1.push(2)

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())
