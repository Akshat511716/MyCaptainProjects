def mostFrequency:
    my_string = input('Please Enter a string : ')
    freq = {}
    for i in my_string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    f = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
    for j, k in f.items():
        print(f"{j} = {k}")    
        

