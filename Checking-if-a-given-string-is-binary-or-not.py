def checkBinary(my_string):
    p = set(my_string)
    s = {'0', '1'}
    if p == s or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")
my_string = '0101010110'
checkBinary(my_string)
