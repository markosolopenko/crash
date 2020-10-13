import re
from string import ascii_lowercase


def three_vowel():
    with open('strings.txt', 'r') as file:
        strings = file.read()
    is_good = []
    for string in strings.split():
        vowel = re.findall(r'[aouie]', string)
        if len(vowel) >= 3:
            is_good.append(True)
        else:
            is_good.append(False)
    return is_good


def double_letter():
    alphabet = ascii_lowercase
    switch = False
    with open('strings.txt', 'r') as file:
        strings = file.read()
    is_good = []
    for string in strings.split():
        for letter in alphabet:
            if letter + letter in string:
                is_good.append(True)
                switch = True
                break
        if switch:
            switch = False
        else:
            is_good.append(False)

    return is_good


def not_contain():
    switch = False
    with open('strings.txt', 'r') as file:
        strings = file.read()
    parts = ['ab', 'cd', 'pq', 'xy']
    is_good = []
    for string in strings.split():
        for part in parts:
            if part in string:
                is_good.append(False)
                switch = True
                break
        if switch:
            switch = False
        else:
            is_good.append(True)
    return is_good


def double_pairs():
    alphabet = ascii_lowercase
    switch1 = False
    switch2 = False
    with open('strings.txt', 'r') as file:
        strings = file.read()
    is_good = []

    for string in strings.split():
        for letter in alphabet:
            for l in alphabet:
                if string.count(letter + l) >= 2:
                    is_good.append(True)
                    switch1 = True
                    break
            if switch1:
                switch1 = False
                switch2 = True
                break
        if switch2:
            switch2 = False
        else:
            is_good.append(False)

    return is_good


def is_between():
    switch = False
    with open('strings.txt', 'r') as file:
        strings = file.read()
    is_good = []

    for string in strings.split():
        for i in range(len(string)):
            if i == len(string) - 2:
                break
            elif string[i] == string[i+2]:
                is_good.append(True)
                switch = True
                break
        if switch:
            switch = False
        else:
            is_good.append(False)
    return is_good


def puzzle1():
    counter = 0
    is_vowel = three_vowel()
    is_double = double_letter()
    is_parts = not_contain()

    for i in range(len(is_vowel)):
        if is_vowel[i] is True and is_double[i] is True and is_parts[i] is True:
            counter += 1
    return counter


def puzzle2():
    counter = 0
    is_double_pairs = double_pairs()
    is_between_letter = is_between()

    for i in range(len(is_double_pairs)):
        if is_double_pairs[i] is True and is_between_letter[i] is True:
            counter += 1
    return counter


if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())

