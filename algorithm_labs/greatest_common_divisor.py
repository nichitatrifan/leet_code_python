
def greatest_common_divisor(m:int, n:int) -> int:
    if m > n:
        divisor = 1
        for i in range(1, n):
            if n % i == 0 and m % i == 0 and i > divisor:
                divisor = i
        return divisor
    else:
        divisor = 1
        for i in range(1, m):
            if n % i == 0 and m % i == 0 and i > divisor:
                divisor = i
    return divisor

if __name__ == '__main__':
    print(greatest_common_divisor(50, 125))