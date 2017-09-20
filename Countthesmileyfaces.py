def count_smileys(arr):
    """Return the valid number of smiley blocks in array."""
    smiles = {':)', ':~)', ':-)', ':-D', ':D', ':~D', ';D', ';)', ';-D', ';~D', ';-)', ';~D'}
    counter = 0
    for i in arr:
        if i in smiles:
            counter += 1
    return counter