def vowcons(string):
    str1 = string.split()  #Split a String into Words
    vowels = 'aeiou'

    for word in str1:
        words = word.lower() #Converting Uppercase Letter into Lowercase
        consonant = 0
        vowel = 0
        for char in words:
            if char not in vowels:
               consonant += 1  #If consonants found in a words it will be increased by 1
            elif char in vowels:
                vowel += 1 #If Vowel found in a words it will be increased by 1
        print(f"'{word}' word has {consonant} Consonants and {vowel} Vowels.")

vowcons("Python is Fun")