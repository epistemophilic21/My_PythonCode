# Finding a Max Even Number, and it's Position in a List.
def minindex(num):
    new = []
    for i in num:
        if i % 2 == 0:  # Finding a Even Number Among a List
            new.append(i)
    x = max(new)  # For Find a Max Number
    for y in range(len(num)):
        if num[y] == x:
            new = []
            break

    new.extend([x, y])  # 'x' is a Max Number, 'y' it's Position
    return new


# Driver Code
if __name__ == '__main__':
    print(minindex([1, 9, 4, 6, 10, 19, 14, 8]))
