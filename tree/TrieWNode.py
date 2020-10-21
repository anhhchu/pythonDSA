from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(dict)
        self.isWord = False
        
class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
         
    def insert(self, word): # O(M*N) 
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word: 
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, word): # O(M) M is number of char in word
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
                
        return True if node and node.isWord else False
        

    def startsWith(self, prefix): 
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix: 
            if char not in node.children:
                return False
            node = node.children[char]
           
        return True

    def delete(self, word): 
        """
        Delete the word in trie, return True if delete successfully, return False if word doesn't exist
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        if not node: 
            return False # word is not in node 
        else:
            node.isWord = False
            return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    words = ['apple', 'apps', 'alps', 'banana', 'berry', 'cherry', 'cranberry']
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    print(trie.root.children)
    print(trie.search('appl')) # False
    print(trie.search('cherry')) # True
    print(trie.startsWith('banna')) # False
    print(trie.delete('banana')) # True
    print(trie.search('banana'))  # False
    print(trie.startsWith('ban')) # False???