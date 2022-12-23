# Python program to remove duplicates from a list of integers [Method 1].
def duplicate(num):
    new = set()
    for i in num:  # Accessing num list
        if i not in new:
            new.add(i)  # Adding i to set
    final = list(new)
    return final


# Driver Code
if __name__ == '__main__':
    print(duplicate([1, 3, 4, 10, 7, 8, 7, 4, 1, 43]))



'''
# Python program to remove duplicates from a list of integers [Method 2].
def duplicate(num):
    num.sort()  # Sorting a List
    new = []

    for i in range(len(num)):
         if num[i] not in new:
            new.append(num[i])
    return new


# Driver Code
if __name__ == '__main__':
    print(duplicate([1, 3, 4, 10, 7, 8, 7, 4, 1, 43])) '''
