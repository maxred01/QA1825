import collections


def file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0
    letter_counter = collections.Counter()

    for line in lines:
        char_count += len(line)
        words = line.split()
        word_count += len(words)
        lower_line = line.lower()
        for char in lower_line:
            if char.isalpha():
                letter_counter[char] += 1

    most_common_letter = letter_counter.most_common(1)[0][0] if letter_counter else ''

    return {
        'lines': line_count,
        'words': word_count,
        'chars': char_count,
        'most_common': most_common_letter
    }
print(file_stats("poem.txt"))
# {'lines': 15, 'words': 210, 'chars': 1250, 'most_common': 'e'}