from sys import stdin

cals = [0]
for line in stdin:
    if line.isspace():
        cals.append(0)
        continue
    cals[-1] += int(line)
#mc = max(range(len(cals)), key=lambda x: cals[x])
#print(f"{cals[mc]}")
mc = max(cals)
print(f"{mc}")
