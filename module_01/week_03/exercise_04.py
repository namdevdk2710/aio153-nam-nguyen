class Queue:
    __queue = []

    def __init__(self, capacity):
        self.__capacity = capacity

    def is_empty(self):
        if (len(self.__queue) == 0):
            return True
        return False

    def is_full(self):
        if (len(self.__queue) >= self.__capacity):
            return True
        return False

    def dequeue(self):
        if (self.is_empty()):
            print("Stack is empty")
            return
        return self.__queue.pop(0)

    def enqueue(self, value):
        if (self.is_full()):
            print("Stack is full")
            return
        self.__queue.append(value)

    def front(self):
        return self.__queue[0]

    def describe(self):
        print(self.__queue)


queue1 = Queue(5)
queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())
