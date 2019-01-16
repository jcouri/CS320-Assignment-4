import sys
print("Assignment #4-1, Joseph Couri, josephmcouri@gmail.com")
with open(sys.argv[1]) as f:
    input = f.readlines()
input = [x.strip() for x in input]
i = 0
while (i < len(input)):
    s = input[i].split()
    if (len(s) != 0):
        t = s[0]
        j = 1
        while (j < len(s)):
            t = t + "," + s[j]
            j = j + 1
        print(t)
    i = i+1
