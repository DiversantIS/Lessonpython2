n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Для n = {n}: {lst} -> {round(sum(lst), 3)}')
