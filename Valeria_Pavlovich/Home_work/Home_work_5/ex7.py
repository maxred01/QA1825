import re
from collections import Counter
def files_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.count('\n') + 1
        words = len(re.findall(r'\b\w+\b', content))
        chars = len(content)
        letters = re.findall(r'\b\w\b', content.lower())
        letter_count = Counter(letters)
        most_common = letter_count.most_common(1)[0][0]
        return {'lines': lines,
                'words': words,
                'chars': chars,
                'most_common': most_common}
stats = files_stats('poem.txt')
print(stats)