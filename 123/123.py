from random import randint as rand

number = int(input('Введи число:'))
lst2 = number
lst = []
a = 0
while number != 0:
    lst1 = [rand(0,100) for i in range(lst2)]
    a +- sum(lst1)
    lst.append(lst1)
    lst1 = []
    number -= 1
    
print('список:', lst, a/lst2**2)