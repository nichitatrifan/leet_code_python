# multiplication of two large numbers
count = 0

def prod(num1, num2):

    n = max(len(str(num1)), len(str(num2)))

    if num1 == 0 or num2 == 0:
        return 0
    elif n <= 1:
        global count
        count += 1

        return num1 * num2
    else:
        m = n//2

        x = num1 // (10**m)
        y = num1 % (10**m)

        w = num2 // (10**m)
        z = num2 % (10**m)

        return prod(x, w)*(10**(2*m)) + (prod(x,z) + prod(w,y))*(10**m) + prod(y,z)

if __name__ == '__main__':
    print(prod(1253, 23103))
    print(count)