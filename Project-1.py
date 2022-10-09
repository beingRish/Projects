"""             Project - 1 Full Stack Web Development using Python
                                 Word Puzzle Game
Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user."""
import random


def main():
    score = 0
    words = ["FATHER", "BREAK", "COUNTRY", "GREEN", "AEROPLANE"]
    words = random.sample(words, k=len(words))

    for word in words:
        score = printPuzzleQuestion(word, score)

    print("Your Score is", score)
    print()


def printPuzzleQuestion(word, score):
    problemWord = shuffleWord(word)
    print("\nArrange the letters to form a valid word:")
    print(problemWord)
    userWord = input()
    print()
    if userWord.upper() == word:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        score -= 1
    return score


def shuffleWord(wrd):
    pw = random.sample(wrd, k=len(wrd))
    return ''.join(pw)


main()
