# coding: utf8
import sys
import re
import os.path
from collections import Counter

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as input_file:
            filedata = input_file.read()
            return filedata
    else:
        return None


def get_most_frequent_words(text):
    words_in_text = re.findall(r'[\w-]+', text)
    dect_words_in_text = Counter(words_in_text)
    count_top_words_in_text = 10
    return dect_words_in_text.most_common(count_top_words_in_text)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:
        print("You should specify a file to analyze!")
        sys.exit(0)
    if load_data(path_to_file):
        data = load_data(path_to_file)
    else:
        print("Incorrect path to the file!")
        sys.exit(0)

    words = get_most_frequent_words(data)

    for word, count in words:
        print('Word ', word, 'repeated in text ', count, 'count')
