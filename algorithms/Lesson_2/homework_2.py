# Homework 2 Algorithms - Julio Fernandez

# Task 1

def reverse_integer(number: int):            ### Slide 15 & 16  @ 1:09 and 1:10
    string2 = str(number)
    if string2[0] == '-':
        return int("-" + string2[:0:-1])
    else:
        return int(string2[::-1])

print(reverse_integer(-128))
print(reverse_integer(876))

# Task 2

def are_anagrams(s1: str, s2: str):   # function sets up 2 variables as strings
    s1 = (s1.lower())
    s2 = (s2.lower())
    if len(s1) != len(s2):          # len function to quickly eliminate strings of unequal length since anagrams
        return False                        # ..... are of equal length
    if sorted(s1) == sorted(s2):    # use sort function to see if strings have same characters
        return True
    else:
        return False

print(are_anagrams('heARt', 'earth'))
print(are_anagrams('rattle', 'battle'))
print(are_anagrams('race', 'care'))


# Task 3
def reverse_words(sentence: str):
    split_words = sentence.split()
    result = []
    for word in split_words:
        result.append(word[::-1])

    return ' '.join(result)    # remember to keep a space between the ' ' to separate the joined words at the end

print(reverse_words('Learning algorithms is fun and useful'))


# Task 4

def repeat_digits(x: str):
    result = ''
    for char in range(len(x)):
        result += int(x[char]) * x[char]

    return result

print(repeat_digits('2603'))

# Task 5

def shortcut(x: str):
        result = ''
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(len(x)):
            if x[i] not in vowels:
                result += x[i]

        return result

print(shortcut('Yesterday'))











