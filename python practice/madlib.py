
with open('madlib.txt', 'r') as lines:
    story = lines.read()

words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and target_start != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
words_map = {}
for word in words:
    answer = input('enter a word for ' + word + ': ')
    words_map[word] = answer
    # words_map.fromkeys('name', 'tobi')
for word in words:
    story = story.replace(word, words_map[word])

print(story)
