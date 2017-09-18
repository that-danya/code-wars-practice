def spin_words(sentence):
    # Your code goes here
    sentence = sentence.split(' ')
    new = []
    for s in sentence:
        if len(s) >= 5:
            s = s[::-1]
        new.append(s)
    return ' '.join(new)
