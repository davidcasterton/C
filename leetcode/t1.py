def yellow(s: str):
    count = {
        'y': 0,
        'e': 0,
        'l': 0,
        'o': 0,
        'w': 0
    }
    for l in s:
        try:
            count[l] += 1
        except KeyError:
            pass

    # print(count)

    min = count['y']
    for k, v in count.items():
        if k == 'l' and v//2 < min:
            min = v//2
        elif v < min:
            min = v
        # print(f'{k=} {v=} {min=}')

    return min

text = "wyollenlw"
print(yellow(text)) # 1

text = "olyewllobaxyllyenw"
print(yellow(text)) # 2

text = "yelooowcde"
print(yellow(text)) # 0
