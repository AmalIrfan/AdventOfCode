from sys import stdin

def get_score(a, b):
    s = 0
    if b == "X":
        s += 1
        if a == "A":
            s += 3
        elif a == "B":
            s += 0
        elif a == "C":
            s += 6
    elif b == "Y":
        s += 2
        if a == "A":
            s += 6
        elif a == "B":
            s += 3
        elif a == "C":
            s += 0
    elif b == "Z":
        s += 3
        if a == "A":
            s += 0
        elif a == "B":
            s += 6
        elif a == "C":
            s += 3
    return s

if __name__ == "__main__":
    ts = 0
    for line in stdin:
        a, b = line.split()
        s = get_score(a, b)
        ts+=s
    print(ts)
