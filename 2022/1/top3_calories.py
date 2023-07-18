from sys import stdin

cals = [0]
for line in stdin:
    if line.isspace():
        cals.append(0)
        continue
    cals[-1] += int(line)
sidx = sorted(range(len(cals)), key=lambda x: cals[x], reverse=True)
print(sum([cals[i] for i in sidx[:3]]))
