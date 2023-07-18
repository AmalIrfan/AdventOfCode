from sys import stdin
from total_score import get_score

def convert(a, b):
    if a == "A":
        if b == "X":
            c = "Z"
        elif b == "Y":
            c = "X"
        elif b == "Z":
            c = "Y"
    elif a == "B":
        if b == "X":
            c = "X"
        elif b == "Y":
            c = "Y"
        elif b == "Z":
            c = "Z"
    elif a == "C":
        if b == "X":
            c = "Y"
        elif b == "Y":
            c = "Z"
        elif b == "Z":
            c = "X"
    return c

if __name__ == "__main__":
    ts = 0
    for line in stdin:
        a, b = line.split()
        c = convert(a, b)
        s = get_score(a, c)
        ts += s
    print(ts)
