def to_jaden_case(string):
    prev_symbol = " "
    list_string = list()
    for symbol in string:
        if prev_symbol == " ":
            list_string.append(symbol.capitalize())
        else:
            list_string.append(symbol.casefold())
        prev_symbol = symbol
    return ''.join(list_string)