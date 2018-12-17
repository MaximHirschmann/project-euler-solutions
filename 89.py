def roman_to_dec(s):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    numbers = [values[char] for char in s]
    total = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    return total + numbers[-1]


def dec_to_roman(n):
    s = ""
    values = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
    for i in reversed(values):
        while n >= i[1]:
            s += i[0]
            n -= i[1]
    return s

romans = [line.replace("\n","") for line in open("storage\\89_roman.txt",'r')]
res = 0
for r in romans:
    res += len(r) - len(dec_to_roman(roman_to_dec(r)))
print(res)
