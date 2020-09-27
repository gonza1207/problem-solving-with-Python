# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(word, k):
    segments = int(len(word) / k)
    for segment in range(segments):
        characters = []
        for idx in range(k):
            character = word[(segment * k) + idx]
            if not character in characters:
                characters.append(character)
        printList(characters)

def printList(characters):
    print("".join(characters))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)