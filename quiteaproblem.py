import sys

while True:
    my_input = sys.stdin.readline()
    if my_input =='':
        break
    elif "problem" in my_input.lower():
        print("yes")
    else:
        print("no")
