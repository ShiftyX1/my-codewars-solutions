def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for symbol in text:
        try:
            result.append(str(alphabet.index(symbol.lower()) + 1))
        except ValueError:
            continue
        
    return ' '.join(result)