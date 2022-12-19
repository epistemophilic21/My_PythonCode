# Python Program to Find Maximum Value of 3 numbers in a list Without Using a Max Function
def maxnumb(numbers):
    length = len(numbers)
    max = 0
    count = 0
    final = []
    numbers.sort()
    if length > 2:    # Calculating a Length of a List
        while count != 3:
            for i in numbers:
                if max < i :  # Finding a Max Number from given List
                   max = i
            final.append(max)  # Appending to Final List
            max = 0
            numbers.pop()  # Removing a Last element from the List
            count += 1
        final.sort()
        return final
    else:
        return numbers  # If it's less than 2 it will return a same List
# Driver Code
if __name__ == '__main__':
    result = maxnumb([9,1,4,6,3,8,10])
    print(result)