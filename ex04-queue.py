

class Element:
    def __init__(self, value:int, previous = None):
        self.__value = value
        self.__previous = previous

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value:int):
        self.__value = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, previous):
        self.__previous = previous


class Stack:
    def __init__(self, max_length: int=4):
        self.__top = None
        self.__count_elements = 0
        self.__max_length = max_length

    @property
    def top(self):
        return self.__top

    def push(self, value: int):
        if self.__count_elements < self.__max_length:
            self.__count_elements += 1
            new_element = Element(value=value, previous=self.__top)
            self.__top = new_element
            
        else:
            print("stack overflow")

    def pop(self):
        if self.__count_elements > 0:
            self.__count_elements -= 1
            poped = self.__top.value
            self.__top = self.__top.previous
            return poped
        else:
            print("empity stack")


new_stack = Stack(max_length=4)
print(f"top element: {new_stack.top}")
new_stack.push(1)
print(f"top element: {new_stack.top.value}")
new_stack.push(2)
print(f"top element: {new_stack.top.value}")
new_stack.push(3)
print(f"top element: {new_stack.top.value}")
new_stack.push(4)
print(f"top element: {new_stack.top.value}")
new_stack.push(5)

print(f"Poped element: {new_stack.pop()}")
print(f"top element: {new_stack.top.value}")
print(f"Poped element: {new_stack.pop()}")
print(f"top element: {new_stack.top.value}")
print(f"Poped element: {new_stack.pop()}")
print(f"top element: {new_stack.top.value}")
print(f"Poped element: {new_stack.pop()}")
print(f"top element: {new_stack.top}")
print(f"Poped element: {new_stack.pop()}")
