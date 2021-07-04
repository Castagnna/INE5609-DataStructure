

class Stack:
    def __init__(self, max_length: int=8):
        self.__max_length = max_length - 1
        self.__pointer = -1
        self.__stack = max_length*[0]

    @property
    def stack(self) -> list:
        return self.__stack

    def push(self, data: int):
        if self.__pointer < self.__max_length:
            self.__pointer += 1
            self.__stack[self.__pointer] = data
        else:
            print("full stack")
    
    def top(self):
        if self.__pointer >= 0:
            return self.__stack[self.__pointer]
        else:
            print("empity stack")

    def pop(self):
        if self.__pointer >= 0:
            self.__pointer -= 1
            return self.__stack[self.__pointer + 1]
        else:
            print("empity stack")


new_stack = Stack(max_length=4)

new_stack.pop()
new_stack.top()
new_stack.push(1)
print(new_stack.stack)
new_stack.push(2)
print(new_stack.stack)
new_stack.push(3)
print(new_stack.stack)
print(f"top: {new_stack.top()}")
print(f"poped: {new_stack.pop()}")
print(f"top: {new_stack.top()}")
print(new_stack.stack)
new_stack.push(33)
print(new_stack.stack)
new_stack.push(4)
print(new_stack.stack)
new_stack.push(5)
print(new_stack.stack)