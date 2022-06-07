def fib_digit(n):
    l = [0, 1]
    for i in range(2, n+1):
        l.append((l[i-1] % 10 + l[i-2] % 10) % 10)
    return l[n]
def main():
    n = int(input())
    print(fib_digit(n))
if __name__ == "__main__":
    main()