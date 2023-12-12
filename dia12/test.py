#Get all combinations of a three character string that uses # and .
for i in range(8):
    s = bin(i)[2:].rjust(3, '0')
    print(s)
    s = s.replace('0', '.')
    s = s.replace('1', '#')
    print(s)
    print('-----')