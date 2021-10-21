import sys
import trie
import json
import string
import pickle
import time

t = trie.SimpleWordTrie()
c = trie.StringTrie()

start = time.time()
with open('./Dataset/in_search_of_lost_time.txt', 'r') as f:
    for line in f:
        line = line.replace("\n", "").lower()
        t.insert(line)
        t.insert(line.translate(str.maketrans('', '', string.punctuation)))
        line = line.split(" ")
        for l in line:
            if line == "" or line == " ":
                continue
            c.insert(line)
            c.insert(l.translate(str.maketrans('', '', string.punctuation)))
    print("Done", time.time() - start)

f = open('trieWord.data', 'wb')
pickle.dump(t, f)
f.close()

f = open('trieChar.data', 'wb')
pickle.dump(c, f)
f.close()