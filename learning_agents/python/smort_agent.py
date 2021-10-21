import pickle
import time
import trie
import json

f = open('smortTrieWord_RJ.data', 'rb')
t = pickle.load(f)
f.close()

data = t.getAllData()

smortTrie = dict()

start = time.time()
for word in data:
    total = sum([data[word][next_word] for next_word in data[word]])
    
    probabilityDistribution = []
    
    for next_word in data[word]:
        prob = float(data[word][next_word] * 1.0 / total)
        probabilityDistribution.append((prob, next_word))

    probabilityDistribution = sorted(probabilityDistribution, key=lambda prob: prob[0], reverse=True)
    # print(probabilityDistribution)

    count = 0
    smortTrie[word] = []

    while len(probabilityDistribution) and count < 10:
        val = probabilityDistribution.pop(0)
        
        grincho = (val[1], round(val[0], 2))

        smortTrie[word].append(grincho)

        count += 1

f = open('rj_trie.json', 'w')
json.dump(smortTrie, f)
f.close()

print("Done", time.time() - start)