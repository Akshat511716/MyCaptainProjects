file_name = input('Input the Filename : ')
file = file_name.split('.')
if file[1] == 'py':
    print("The extensio of the file is : 'python' ")
else:
    print("Invalid format entered!")
