size = eval(input('Enter the number of elements : '))
mylist = []
for i in range(size):
    element = int(input(f'Number {i+1} :'))
    mylist.append(element)
for num in mylist:
    if num >= 0:
        print(num, end = " ")
