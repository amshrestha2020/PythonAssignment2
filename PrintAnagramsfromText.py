'Write a code that will put out the anagrams (words that use the same letters) from a paragraph of text.'

from collections import Counter, defaultdict

words = """It’s very suspicious that the term ‘school master’ is an anagram for ‘the classroom,’ almost like they made it that way on purpose."""

print("Paragraph containing anagrams :", words)
# sorted_words = list(set(words.split()))
# search_anagrams = defaultdict(list)
# anagrams = []

# def anagram(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         histogram = tuple(Counter(word).items()) # build a hashable histogram
#         anagrams[histogram].append(word)
#     return list(anagrams.values())

# print("Anagrams words :", words)

def anagrams(words, test_string):
    print("*************************")
    print("Paragraph to test anagram words :", words)
    print("*************************")

    'Find th list of anagrams in the paragraph'
    test_words = list(filter(lambda x: (Counter(test_string) == Counter(x)), words))

    'Print the list of anagrams'
    print("*************************")
    print("Test words =", test_words)
    print("*************************")

def Driver():
    words = ['school master', 'classroom']
    test_string = "classroom"
    anagrams(words, test_string)

if __name__ == "__main__" :
    Driver()
