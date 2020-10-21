'''
Implement a Trie class without a TrieNode class
'''
class Trie(object):
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True # $ signals end of the trie

    def search(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return '$' in node

    def startsWith(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

if __name__ == '__main__':
    words = ['apple', 'apps', 'alps', 'banana', 'berry', 'cherry', 'cranberry']
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    print(trie.trie)
    print(trie.search('appl')) # False
    print(trie.search('cherry')) # True
    print(trie.startsWith('banna')) # False
    #print(trie.delete('banana')) # True
    print(trie.search('banana'))  # False
    print(trie.startsWith('ban')) # False???