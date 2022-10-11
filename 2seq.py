sep = input("Введите разделитель элементов списка ( , - разделитель по умолчанию): , ; / \n")
if sep !=',' and sep !=';' and sep !='/':
    sep = ','
listA = input("Введите элементы списка 1 \n").split(sep)
print(type(listA))
print(listA)
listA = list(set(listA))
print(listA)
