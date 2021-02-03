NUMBER_OF_PER_LINE = 8
count = 0
num = 2

while num <= 1000:
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        count = count + 1

        if count % NUMBER_OF_PER_LINE != 0:
            print(num, end=" ")

        else:
            print(num)

    num = num + 1

