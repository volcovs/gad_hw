dictionar = {}
for num in range(1, 11):
    dictionar[num] = num * num

print(dictionar)

dictionar = {num: num*num for num in range(1, 11)}
print(dictionar)

dictionar_2 = {num: num*num for num in range(1, 11) if num%2 == 0}
print(dictionar_2)
