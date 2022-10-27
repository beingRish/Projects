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
