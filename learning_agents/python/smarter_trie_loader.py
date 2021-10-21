import sys
import trie
import json
import string
import pickle
import time

t = trie.SmortWordTrie(5)

punctuations = '''!()[]{};:"\,<>/?@#$%^&*_~'''

start = time.time()
counter = 0
# MAX_POINTS = sum(1 for line in open('Dataset/in_search_of_lost_time.txt'))
MAX_POINTS = sum(1 for line in open('Dataset/romeo_and_juliet.txt'))

# with open('./Dataset/in_search_of_lost_time.txt', 'r') as f:
with open('./Dataset/romeo_and_juliet.txt', 'r') as f:
    for line in f:
        counter = counter + 1
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%% %d/%d" % ('#'*int((counter / (MAX_POINTS/20))), float(counter/MAX_POINTS*100), counter, MAX_POINTS))
        sys.stdout.flush()

        line = line.replace("\n", "").lower()
    
        for p in punctuations:
            line = line.replace(p, '')

        lines = line.split(".")
        
        for line in lines:
            t.insert(line)

    print("\nDone", time.time() - start)

f = open('smortTrieWord_RJ.data', 'wb')
pickle.dump(t, f)
f.close()