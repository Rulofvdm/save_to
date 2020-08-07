import random
from sys import maxunicode

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    random_index = random.randint(0, len(word)-1)
    print('Guess the word: '+word[:random_index]+"_"+word[random_index+1:])
    return word


def get_user_input():
    return input('Guess the missing letter: ')


def show_answer(answer, selected_word):
    print("The word was: " + selected_word)
    if answer in selected_word:
        print("Well done! You are awesome!\n")
    else:
        print("Wrong! Do better next time.\n")


def ask_file_name():
    file = input("Words file? [leave empty to use short_words.txt] : \n")
    if file == "":
        file = "short_words.txt"
    return file


def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    show_answer(answer, word)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)