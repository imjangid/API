from api.settings import BASE_DIR
from os.path import join
import multiprocessing


files = join(BASE_DIR, "Static")






def get_word(text):
    sort = open(join(files, "sorted.txt"), "r+")
    orig = open(join(files, "original.txt"), "r+")
    words = list()
    lines = []
    text = "".join(sorted(text))
    for x, line in enumerate(sort.readlines()):
        if line.strip().startswith(text):
            lines.append(x)
    for x, line in enumerate(orig.readlines()):
        line = line.strip("\n")
        if x in lines:
            words.append(line)
    words = list(filter(lambda x : len(x) <= len(text)+1, words))
    print(words)
    sort.close()
    orig.close()
    return words
