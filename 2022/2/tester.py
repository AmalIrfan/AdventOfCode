from total_score import get_score

#for a in "ABC":
#    for b in "XYZ":
#        print(a, b, get_score(a, b))

from new_rules import convert

for a in "ABC":
    for b in "XYZ":
        c = convert(a, b)
        print(a, b, c, get_score(a, c))
