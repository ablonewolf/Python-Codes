def take_input():
    return input("Enter the sentence: ")


def check_if_character(char):
    return ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122))


def count_vowel(sentence):
    return len([char for char in sentence if char in 'aeiou' or char in 'AEIOU'])


def count_consonent(sentence):
    return len([char for char in sentence if (check_if_character(char)) and (char not in 'aeiou' and char not in 'AEIOU')])


def main_menu():
    sentence = take_input()
    if (len(sentence.split(' ')) > 1):
        print(f"Number of vowels in the sentence: {count_vowel(sentence)}")
        print(
            f"Number of consonants in the sentence: {count_consonent(sentence)}")
    else:
        print(f"Sentence is too short. Please try again")
        main_menu()


main_menu()
