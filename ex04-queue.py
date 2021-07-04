

class Element:
    def __init__(self, value:int, next = None):
        self.__value = value
        self.__next = next

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value:int):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Queue:
    def __init__(self, max_length: int=4):
        self.__head = None
        self.__tail = None
        self.__count_elements = 0
        self.__max_length = max_length

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def enqueue(self, value: int):
        if self.__count_elements >= self.__max_length:
            print("queue overflow")
            return
        
        self.__count_elements += 1
        new_element = Element(value=value, next=None)

        if self.__count_elements == 0:
            self.__head = new_element
            self.__tail = new_element
        else:
            self.__tail.next = new_element
            self.__tail = new_element            

    def dequeue(self):
        if self.__count_elements > 0:
            self.__count_elements -= 1
            poped = self.__top.value
            self.__top = self.__top.previous
            return poped
        else:
            print("empity queue")


new_queue = Queue(max_length=4)
print(f"top element: {new_queue.top}")
new_queue.push(1)
print(f"top element: {new_queue.top.value}")
new_queue.push(2)
print(f"top element: {new_queue.top.value}")
new_queue.push(3)
print(f"top element: {new_queue.top.value}")
new_queue.push(4)
print(f"top element: {new_queue.top.value}")
new_queue.push(5)

print(f"Poped element: {new_queue.pop()}")
print(f"top element: {new_queue.top.value}")
print(f"Poped element: {new_queue.pop()}")
print(f"top element: {new_queue.top.value}")
print(f"Poped element: {new_queue.pop()}")
print(f"top element: {new_queue.top.value}")
print(f"Poped element: {new_queue.pop()}")
print(f"top element: {new_queue.top}")
print(f"Poped element: {new_queue.pop()}")
