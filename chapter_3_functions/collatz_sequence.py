 # последовательность коллатца

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

print('Введите число для последовательности Коллатца')
number = int(input())
collatz(number)



