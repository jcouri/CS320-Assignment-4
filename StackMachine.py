class StackMachine:
    def __init__(self):
        self._array = []
    def push(self, item):
        self._array.append(item)
    def pop(self):
        if (len(self._array) != 0):
            return self._array.pop()
    def add(self):
        if (len(self._array) >= 2):
            x = self.pop()
            y = self.pop()
            self.push(x+y)
    def sub(self):
        if (len(self._array) >= 2):
            x = self.pop()
            y = self.pop()
            self.push(x-y)
    def mul(self):
        if (len(self._array) >= 2):
            x = self.pop()
            y = self.pop()
            self.push(x*y)
    def div(self):
        if (len(self._array) >= 2):
            x = self.pop()
            y = self.pop()
            self.push(x/y)
    def mod(self):
        if (len(self._array) >= 2):
            x = self.pop()
            y = self.pop()
            self.push(x%y)
