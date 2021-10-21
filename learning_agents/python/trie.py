class node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.count = 0

class StringTrie:
    def __init__(self):
        self.head = node("")

    def insert(self, new_string):
        cur_node = self.head    
        for s in new_string:
            if s not in cur_node.children:
                cur_node.children[s] = node(s)
            cur_node.children[s].count += 1
            cur_node = cur_node.children[s]

    def search(self, word):
        word = word.lower()
        cur_node = self.head
        for s in word:
            if s not in cur_node.children:
                return False
            cur_node = cur_node.children[s]
        
        return True


class SimpleWordTrie:
    def __init__(self):
        self.trie = dict()

    def insert(self, string):
        words = string.split(" ")
        for i in range(len(words)-1):
            if words[i] == "" or words[i] == " ":
                continue
            if words[i+1] == "" or words[i+1] == " ":
                continue

            if words[i] not in self.trie:
                self.trie[words[i]] = dict()

            if words[i+1] not in self.trie[words[i]]:
                self.trie[words[i]][words[i+1]] = 0

            self.trie[words[i]][words[i+1]] += 1
    
    # def search(self, string):
    #     words = string.lower().split(" ")
    #     data = [key for key in self.trie]
    #     for i in range(len(words)-1):
    #         if words[i] not in data:
    #             return False
    #         data = self.trie[words[i]]
    #     return True
    
    def nextWords(self, string):
        words = string.split(" ")
        return self.trie[words[-1]] if words[-1] in self.trie else []
    
    def getAllData(self):
        return self.trie

class SmortWordTrie:
    def __init__(self, k):
        self.trie = dict()
        self.k = k

    def insert(self, string):
        words = string.split(" ")
        for i in range(len(words)-1):          
            for j in range(max(0, i-self.k), i+1):
                preceedingPhrase = ' '.join(words[j:i])

                if preceedingPhrase == "" or preceedingPhrase == " ":
                    continue
                if words[i] == "" or words[i] == " ":
                    continue

                if preceedingPhrase not in self.trie:
                    self.trie[preceedingPhrase] = dict()
                
                if words[i] not in self.trie[preceedingPhrase]:
                    self.trie[preceedingPhrase][words[i]] = 0
                
                self.trie[preceedingPhrase][words[i]] += 1

    
    # def search(self, string):
    #     words = string.lower().split(" ")
    #     data = [key for key in self.trie]
    #     for i in range(len(words)-1):
    #         if words[i] not in data:
    #             return False
    #         data = self.trie[words[i]]
    #     return True
    
    def nextWords(self, string):
        words = string.split(" ")
        sentence = words[max(len(words)-1-k,0):]
        return self.trie[sentence] if sentence in self.trie else []
    
    def getAllData(self):
        return self.trie

class WordTrie:
    def __init__(self):
        self.head = node("")

    def insert(self, new_string):
        cur_node = self.head    
        words = new_string.split(" ")
        for word in words:
            if word == "" or word == " ":
                continue
            if word not in cur_node.children:
                cur_node.children[word] = node(word)
            cur_node = cur_node.children[word]

    def search(self, string):
        cur_node = self.head

        words = string.lower().split(" ")
        for word in words:
            if word == "" or word == " ":
                continue
            if word not in cur_node.children:
                return False
            cur_node = cur_node.children[word]


        return True

    def _getNode(self, string):
        string = string.lower()
        cur_node = self.head

        words = string.lower().split(" ")
        for word in words:
            if word == "" or word == " ":
                continue
            cur_node = cur_node.children[word]
        
        return cur_node

    def nextWords(self, string):
        string = string.lower()
        if not self.search(string):
            return []
        
        suggestions = []
        cur_node = self._getNode(string)
        
        for words in cur_node.children:
            suggestions.append(words)
        
        return suggestions
