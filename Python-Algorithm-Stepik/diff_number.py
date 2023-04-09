def algoritm(n):
    count = n
    list_numbers = []
    if n == 1:
        list_numbers.append(1)
    else:
        for i in range(1, n):
            count = count - i
            if count >= (i+1):
                list_numbers.append(i)
            else:
                list_numbers.append(count+i)
                break
    return list_numbers

def main():
    n = int(input())
    result = algoritm(n)
    print(len(result))
    print(*result)


if __name__ == "__main__":
    main()
