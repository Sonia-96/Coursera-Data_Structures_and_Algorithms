#python3


import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_value = []

    def Push(self, a):
        if not self.max_value:
            self.max_value.append(a)
        elif a >= self.max_value[-1]:
            self.max_value.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] == self.max_value[-1]:
            self.max_value.pop()
        self.__stack.pop()

    def Max(self):
        return self.max_value[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
