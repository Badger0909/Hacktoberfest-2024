def file_handler(file):
    with open(file, 'r') as f:
        text = f.read()
        words = text.split()
        return words

def separator():
    print(f'\n{"-"*10}\n')

def find_Palindromes(words):
    palindromes = [word for word in words if word==word[::-1]]
    print(f'Total Palindromes {len(palindromes)}. They are: {palindromes}')
    separator()

def top_longest_words(words, top_n=5):
    for word in sorted(words, key=len, reverse=True)[:top_n]:
        print(f'{word}: {len(word)}')
    separator()

def word_frequency(words):
    words = [word.lower() for word in words]
    for word in words:
        print(f'{word}: {words.count(word)}')
    separator()

words = file_handler('wordlist.txt')

find_Palindromes(words)
top_longest_words(words)
word_frequency(words)
