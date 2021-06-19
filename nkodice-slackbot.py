dice = ['お', 'ち', 'ま', 'う', 'ん', 'こ']
all_rolls = set()
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    sorted_roll = sorted([i]+[j]+[k]+[l]+[m])
                    a = ''
                    for r in sorted_roll:
                        a += str(dice[r])
                    all_rolls.add(a)
for roll in all_rolls:
    result = roll
    if roll.count('う') >= 1 and roll.count('ん') >= 1 and roll.count('ち') >= 1:
        result += ':n7:'
    if roll.count('う') >= 1 and roll.count('ん') >= 1 and roll.count('こ') >= 1:
        result += ':n6:'
    if roll.count('ち') >= 1 and roll.count('ん') >= 1 and roll.count('こ') >= 1:
        result += ':n4:'
    if roll.count('お') >= 1 and roll.count('ま') >= 1 and roll.count('ん') >= 1 and roll.count('こ') >= 1:
        result += ':n3:'
    elif roll.count('ま') >= 1 and roll.count('ん') >= 1 and roll.count('こ') >= 1:
        result += ':n5:'
    if roll.count('お') >= 1 and roll.count('ち') >= 2 and roll.count('ん') >= 2:
        result += ':n1:'
    elif roll.count('ち') >= 2 and roll.count('ん') >= 2:
        result += ':n2:'
    print(result)
