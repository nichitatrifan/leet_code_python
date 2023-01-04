if __name__ == '__main__':
    height = 8

    for i in range(height//2):
        print(" " * (height - i), "*" * (2*i + 1))
    for i in range(height//2, -1, -1):
        print(" " * (height - i), "*" * (2*i + 1))