def fingerprint(n):
    mem = {}
    res = []
    count = 0
    for i in str(n):
        if i in mem:
            res.append(mem[i])
        else:
            res.append(count)
            mem[i] = count
            count += 1
    return tuple(res)

with open('storage//98_words.txt','r') as f:
    words = eval(f.read())

temp_anagrams = {tuple(sorted(i)):[] for i in words}
for i in words:
    temp_anagrams[tuple(sorted(i))].append(i)
anagrams = [v for k, v in temp_anagrams.items() if len(v) > 1]

squares = [i*i for i in range(10**5)]
digits = {fingerprint(i):[] for i in squares} # fingerprints of the squares
for i in squares:
    digits[fingerprint(i)].append(i)

res = 0
for anagram in anagrams:
    word = anagram[0]
    fp = fingerprint(word)
    if fp not in digits:
        continue
    for square in digits[fp]:
        letter_digit = {word[i]:str(square)[i] for i in range(len(word))}
        if letter_digit[anagram[1][0]] == '0':
            continue
        new_num = int(''.join([letter_digit[i] for i in anagram[1]]))
        if new_num in squares:
            maximum = max(square, new_num)
            if res < maximum:
                res = maximum
print(res)