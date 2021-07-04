

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
        
        new_element = Element(value=value, next=None)

        if self.__count_elements == 0:
            self.__head = new_element
            self.__tail = new_element
        else:
            self.__tail.next = new_element
            self.__tail = new_element

        self.__count_elements += 1           

    def dequeue(self):
        if self.__count_elements == 0:
            print("empity queue")
            return

        unlined = self.__head.value

        if self.__count_elements == 1:
            self.__tail = None
            self.__head = None

        else:
            self.__head= self.__head.next

        self.__count_elements -= 1

        return unlined


new_queue = Queue()
print(f"head: {new_queue.head}, tail: {new_queue.tail}")
new_queue.enqueue(1)
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
new_queue.enqueue(2)
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
new_queue.enqueue(3)
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
new_queue.enqueue(4)
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
new_queue.enqueue(5)

print(f"Unlined element: {new_queue.dequeue()}")
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
print(f"Unlined element: {new_queue.dequeue()}")
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
new_queue.enqueue(5)
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
print(f"Unlined element: {new_queue.dequeue()}")
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
print(f"Unlined element: {new_queue.dequeue()}")
print(f"head: {new_queue.head.value}, tail: {new_queue.tail.value}")
print(f"Unlined element: {new_queue.dequeue()}")
print(f"head: {new_queue.head}, tail: {new_queue.tail}")
