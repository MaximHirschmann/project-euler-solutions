from Utils import pentagonalNumber, isPentagonalNumber

def find():
    pentagonal = []
    i = 1
    while True:
        pent = pentagonalNumber(i)
        for j in pentagonal:
            if isPentagonalNumber(abs(pent-j)) and isPentagonalNumber(pent+j):
                return (pent-j)
        pentagonal.append(pent)
        i += 1

print(find())