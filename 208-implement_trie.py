class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:

    def __init__(self):
        self.t = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.t
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.eow = True

    def search(self, word: str) -> bool:
        ptr = self.t
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.eow
    def startsWith(self, prefix: str) -> bool:
        ptr = self.t
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True