def multiplication(number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input('Введите число: '))
print(f'Пусть N = {n}, ' , end = ' тогда ')
for i in range(1, n + 1):
    if i == n: 
        print(f'{multiplication(i)}')
    else:
        print(f'{multiplication(i)}', end = ', ')