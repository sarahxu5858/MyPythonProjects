def split_half(str0):
    a = (len(str0)/2).__ceil__()
    str1 = str0[:int(a)]
    str2 = str0[int(a):]
    return str2+str1

print(split_half('aaaacbbbb'))


def unique_char(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    d = {}

    for l in string:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    print(d)
    for k, v in d.items():
        if v == 1:
            return True
    return False

print(unique_char('asdf'))
