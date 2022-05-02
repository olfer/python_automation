# Игра в угадывание чисел.
import random
secret_number = random.randint(1, 20)
print('Число загадано в диапазоне от 1 до 20. попробуй его угадать.')

# предоставить игроку 6 попыток угадать число.\

for guesses_taken in range(1, 7):
    print('Ваш вариант:')
    guess = int(input())

    if guess < secret_number:
        print('Предложенное число меньше загаданного.')
    elif guess > secret_number:
        print('Предложенное число больше загаданного.')
    else:
        break # Соответсвует правильному ответу!
        
if guess == secret_number:
    print('Верно! Количество попыток: ' + str(guesses_taken))
else:
    print('Нет. Было задумано число ' + str(secret_number))