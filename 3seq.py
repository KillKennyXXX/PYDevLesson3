sep = input("Введите разделитель элементов списка ( , - разделитель по умолчанию): , ; / \n")
if sep !=',' and sep !=';' and sep !='/':
    sep = ','
listA = input("Введите элементы списка 1 \n").split(sep)
print(type(listA))
print(listA)
listB = input("Введите элементы списка 2 \n").split(sep)
print(type(listB))
print(listB)
for i in listB:
    if i in listA:
        listA.remove(i)
print(f'Финальный список {listA}')