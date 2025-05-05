import sys

current_word = None

current_count = 0

for line in sys.stdin:
    word, one = line.strip().split(',')
    count = int(one)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word},{current_count}")
        current_word = word
        current_count = count

if current_word:
    print(f"{current_word},{current_count}")
