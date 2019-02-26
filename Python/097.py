def last_digits_power2(digits, exponent):
    length = 4*(5**(digits-1))   # length of cycle of repeating last digits
    position = (exponent-digits)%length # position in the cycle
    return (2**(digits + position)) % (10**digits)

def last_digits_of_mersenne(factor, exponent, num_digits):
    digits = last_digits_power2(num_digits, exponent)
    return (factor * digits + 1) % (10**num_digits)

print(last_digits_of_mersenne(28433, 7830457, 10))