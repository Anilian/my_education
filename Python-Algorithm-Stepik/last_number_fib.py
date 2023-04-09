def fib_digit(n):
    arr = []
    f0 = 0
    f1 = 1
    arr.append(f0)
    arr.append(f1)
    for i in range(2,n):
        k = arr[i-1]+arr[i-2]
        fk = k%10
        arr.append(fk)
    fn = (arr[n-2]+arr[n-1])%10 

    return fn


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()