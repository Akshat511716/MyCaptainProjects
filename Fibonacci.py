total_number = int(input('Enter the number you want the series upto : '))
if total_number == 1:
    print('0')
elif total_number == 2:
    print('0')
    print('1')
else:
    first = 0
    second = 1
    print('0')
    for i in range((total_number)-2):
        print(second)
        sum = first + second
        first = second
        second = sum    
        
