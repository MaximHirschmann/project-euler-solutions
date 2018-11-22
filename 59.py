from itertools import product

start = time()

def to_text(values, key):
    s = ''
    for i, ascii in enumerate(values):
        s += chr(int(ascii) ^ key[i%3])
    return s

def sum_text(text):
    return sum([ord(i) for i in text])

with open("storage//59_encryption.txt","r") as f:
    encrypted = eval(f.read())

for key in product(range(97,123), repeat = 3):
    text = to_text(encrypted, key)
    if text.find(' the ') >= 0:
        print('KEY: ',''.join([chr(i) for i in key]))
        print('TEXT: ',text)
        print('SUM: ', sum_text(text))
        break