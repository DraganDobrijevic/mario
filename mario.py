from cs50 import get_int

while True:
    b = get_int("Height: ")
    if b > 0 and b < 9:
        break
    else:
        True

for i in range(b):
    for j in range(b - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()

    
