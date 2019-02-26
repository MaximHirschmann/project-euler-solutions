def same_digits(a,b,c,d,e,f):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c)) == sorted(str(d)) == sorted(str(e)) == sorted(str(f))

i = 1
while True:
    if same_digits(i,2*i,3*i,4*i,5*i,6*i):
        print(i)
        break
    i += 1