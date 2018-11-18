from math import gcd

def cancel_digits(a,b):
    a,b = str(a),str(b)
    i = 0
    while i<len(a):
        index = a.find(a[i])
        if index != -1:
            b=b.replace(a[i],"",1)
            a=a.replace(a[i],"",1)
        i += 1
    return (int(a),int(b))

numerator = 1
denominator = 1
for a in range(11,100):
    for b in range(10,a):
        if not(a%10==0 and b%10==0):
            canceled = cancel_digits(a,b)
            c = canceled[0]
            d = canceled[1]
            if c!= 0 and b/a==d/c and b!=d:
                numerator*=d
                denominator*=c

gcd_res = gcd(numerator,denominator)
numerator = int(numerator/gcd_res)
denominator = int(denominator/gcd_res)
print('Result:',denominator)