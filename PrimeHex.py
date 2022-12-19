# Program to find which characters of a hexadecimal number correspond to prime numbers.
def primehex(varchar):
    result = []
    new_list = []
    result.extend(varchar) # Extending a varchar value and appending into result list
    n = 15  # Range till 15
    num = '0123456789'
    hex = { "A":10, "B": 11, "C": 12,"D":13,"E":14,"F":15 }

    for vchar in result:
        if vchar in hex:  # If it's a Alphabet it will check the values in 'hex' set
            flag = False
            x = hex[vchar]
            for i in range(2, n):
                if x % i == 0: # Checking whether given key value is divisible by given range
                    if x != i:
                        new_list.append('True')
                        flag = True
                        break
                    else:
                        continue
                else:
                    continue

            if flag  ==  False:
                new_list.append('False')

        elif vchar in num:  # If it's a Number it will check the values in num string.
            flag = False
            for i in range(2, n):
                vchar = int(vchar)
                if vchar % i == 0: # Checking whether given number is divisible by given range.
                    if vchar != i:
                        new_list.append('True')
                        flag = True
                        break
                    else:
                        continue
                else:
                    continue

            if flag == False:
                new_list.append('False')

        else:
            if vchar not in hex: # Checks whether given alphabet is out of range.
               print(f"'{vchar}' is Not the Part Of Part of HexaDecimal.")

    return new_list
# Driver Code
if __name__ == '__main__':
    final = primehex("ABC468")  # Please Enter a UpperCase Letters bcz I forgot to Add a Condition ;)
    print(final)
