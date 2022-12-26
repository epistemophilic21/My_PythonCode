# Python program to find the string consisting of all the words whose lengths are prime numbers.
def prime(string):
    new = []
    flag = False
    word = string.split()  # Split a Sentence into a word
    for char in word:
        x = len(char)
        for i in range(2, x):
            if x % i == 0:
                if x == i:
                    continue
                flag = True
                break
            else:
                flag = False
                continue
        if not flag:  # If it's prime append to n
            new.append(char)
    print("Original Text:")
    print(string)
    print()
    print("Lengths are prime numbers in the said string:")
    return new


# Driver Code
if __name__ == '__main__':
    # Note : Spaces also counts!
    final = prime("The quick brown fox jumps over the lazy dog")
    print(final)
