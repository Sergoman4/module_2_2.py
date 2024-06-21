first = int(input('введите номер : '))
second = int(input('введите номер : '))
third = int(input('введите номер : '))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)