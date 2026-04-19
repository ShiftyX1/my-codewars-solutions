def accum(st):
    return ''.join([elem.capitalize() for elem in [i * x + '-' for i, x in enumerate(st, 1)]])[:-1]
