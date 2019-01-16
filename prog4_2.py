import StackMachine
import sys
print("Assignment #4-2, Joseph Couri, josephmcouri@gmail.com")
sm = StackMachine
stack = sm.StackMachine()
with open(sys.argv[1]) as f:
    input = f.readlines()
input = [x.strip() for x in input]
i = 0
while (i < len(input)):
    s = input[i].split()
    if(len(s) == 2):
        if (s[0] == 'push'):
            isInt = "yes"
            isFloat = "yes"
            try:
                int(s[1])
            except ValueError:
                isInt = "no"
            try:
                float(s[1])
            except ValueError:
                isFloat = "no"
            if (isInt == 'yes'):
                stack.push(int(s[1]))
            elif (isFloat == 'yes'):
                stack.push(float(s[1]))
    if(len(s) == 1):
        if (s[0] == 'pop'):
            print(stack.pop())
        if (s[0] == 'add'):
            stack.add()
        if (s[0] == 'sub'):
            stack.sub()
        if (s[0] == 'mul'):
            stack.mul()
        if (s[0] == 'div'):
            stack.div()
        if (s[0] == 'mod'):
            stack.mod()
    i = i+1

