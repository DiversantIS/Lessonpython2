from decimal import Decimal
num = Decimal(input('Вводим вещественное число\n'))
 
digits = num.as_tuple().digits
print(f'Сумма числа равна \n{sum(digits)}')