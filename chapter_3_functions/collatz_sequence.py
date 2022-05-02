 # последовательность коллатца

def collatz(number):
    print('Введите число для последовательности Коллатца')
    number = int(input())
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
    print('Исследовать еще одну последовательность? (Введите Да или Нет)')
    repeat = input()
    if repeat == 'да':
        collatz(number)
    else:
        print('Надеюсь все прошло хорошо!')


repeat = ''
number = 0
collatz(number)





