def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ''
    idx = alphabet.find(letter)
    if idx == -1:           #not found
        print("error;" , letter, "is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase
    letter = ''
    if idx >= len(alphabet):
        print("error:",idx, "its to large")
    elif idx <0:
        print("error:", idx, "is too small")
    else:
        letter = alphabet[idx]
    return letter

#testing functions with mapper.py

from mapper import*

print(letterToIndex('P'))
print(indexToLetter(10))
