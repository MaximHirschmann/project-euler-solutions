def sup(n):
    print(n,'super')
    return 'sup'
def testing(n):
    print(n, 'testing')
    return 'testing'

num = 2
l = [sup(num),testing(num)]
for i in l:
    i()