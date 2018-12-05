# assumes each digit appears only once
nums = []
# dict with i:set() for every digit i that appears
count = {}
with open('storage//79_keylog.txt','r') as f:
    for line in f:
        code = line.replace('\n','')
        for digit in code:
            count[digit] = set()
        nums.append(code)

for num in nums:
    for digit in range(1,len(num)):
        for digit_before in range(digit):
            count[num[digit]].add(num[digit_before])
# sorts keys by length of values
temp = sorted(count.items(), key=lambda kv: len(kv[1]))
# joins keys
res = ''.join([item[0] for item in temp])
print(res)