def solution(s):
    if len(s) == 0:
        return list()
    elif len(s) % 2 == 0:
        return [s[i:i + 2] for i in range(0, len(s), 2)]
    elif len(s) % 2 != 0:
        itog = [s[i:i + 2] for i in range(0, len(s), 2)]
        itog[-1] += '_'
        return itog