# https://www.hackerrank.com/challenges/the-minion-game/problem

def calculate_score(word, predicate):
    score = 0
    index = 0
    length = len(word)
    for letter in word:
        if predicate(letter):
            score += (length - index)
        index = index + 1
    return score


def is_vowel(character):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return character in vowels


def minion_game(word):
    stuart_score = calculate_score(word, lambda char: not is_vowel(char))
    kevin_score = calculate_score(word, is_vowel)

    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))
    else:
        print("Stuart " + str(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)
