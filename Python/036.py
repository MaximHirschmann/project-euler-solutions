from Utils import isPalindrom

print(sum([i for i in range(1,1000000) if isPalindrom(str(i)) and isPalindrom(bin(i)[2:])]))