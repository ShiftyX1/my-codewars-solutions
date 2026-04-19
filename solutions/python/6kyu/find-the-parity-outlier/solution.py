def find_outlier(integers):
    even = []
    odds = []
    i = 0
    for number in integers:
        if number % 2 == 0:
            even.append(number)
        else:
            odds.append(number)
        i += 1
        if (i >= 3) and ((len(even) == 1) or (len(odds) == 1)):
            break
    if len(even) == 1:
        return even[0]
    elif len(odds) == 1:
        return odds[0]
    else:
        return None