
# even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"




# Prime or not
def PrimeOrNot(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

    if c == 2: 
        return "Prime"
    else:
        return "Not a Prime"






