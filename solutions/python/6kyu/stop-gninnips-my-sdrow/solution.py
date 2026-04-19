def spin_words(sentence):
    words_list = sentence.split(' ')
    new_words_list = list()
    for word in words_list:
        if len(word) >= 5:
            new_words_list.append(word[::-1])
        else:
            new_words_list.append(word)
    return " ".join(new_words_list)