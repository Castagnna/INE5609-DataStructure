

class Queue:
    def __init__(self, max_length: int=8):
        self.__max_length = max_length
        self.__head = 0
        self.__tail = 0
        self.__count_elements = 0
        self.__queue = (max_length)*[0]

    @property
    def queue(self) -> list:
        return self.__queue

    def enqueue(self, data: int):
        # entra na fila
        if self.__count_elements < self.__max_length:
            self.__count_elements += 1
            self.__queue[self.__tail] = data
            self.__tail = (self.__tail + 1) % self.__max_length
        else:
            print("full queue")

    def dequeue(self):
        if self.__count_elements > 0:
            self.__count_elements -= 1
            self.__queue[self.__head] = -1
            self.__head = (self.__head + 1) % self.__max_length
        else:
            print("empity queue")

    def status(self):
        print(f"head: {self.__head}, element: {self.__queue[self.__head]}")
        print(f"tail: {self.__tail}, element: {self.__queue[self.__tail]}")
        print(f"queue: {self.queue}")


new_queue = Queue(max_length=4)
new_queue.status()

new_queue.enqueue(1)
new_queue.status()

new_queue.enqueue(2)
new_queue.status()

new_queue.enqueue(3)
new_queue.status()

new_queue.enqueue(4)
new_queue.status()

new_queue.enqueue(5)
new_queue.status()

new_queue.dequeue()
new_queue.status()

new_queue.enqueue(5)
new_queue.status()

new_queue.dequeue()
new_queue.status()

new_queue.dequeue()
new_queue.status()

new_queue.dequeue()
new_queue.status()

new_queue.dequeue()
new_queue.status()

new_queue.dequeue()
new_queue.status()