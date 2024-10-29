from functools import cache
class Solution:
    # SOLUTION: backtrack with memo (which I guess is DP)
    # TC: O(N * M * K) -- N = length of s * M = # of words in wordDict * K = average size of word in word dict ?
        # at most we only calculate bt(l,r) once because of memoization.
    # SC: O(N) -- memoization & call stack size
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_size = len(max(wordDict, key = len))
        wordDict = set(wordDict)

        @cache
        def bt(l,r):
            if r == len(s) and l == r:
                return True
            while r <= l + max_size and r < len(s):
                if s[l:r+1] in wordDict:
                    if (bt(r+1, r+1)):
                        return True
                r += 1
            return False
        return bt(0,0)
    
class Solution:
    # SOLUTION #2: same as above, but utilizing trie
    # TC: O(N*M*K) -- because of trie, we should only be bailing out much sooner on invalid possibilities instead of always going from l:max_size+1
    # SC: O(N) -- call stack + memoization + trie
    class TrieNode:
        def __init__(self):
            self.eow = False
            self.children = {}
    class Trie:
        def __init__(self):
            self.trie = TrieNode()
        def insert(self, s):
            ptr = self.trie
            for ch in s:
                if ch not in ptr.children:
                    ptr.children[ch] = TrieNode()
                ptr = ptr.children[ch]
            ptr.eow = True
    def startsWith(self, s):
        ptr = self.trie
        for ch in s:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return True
    def contains(self, s):
        ptr = self.trie
        for ch in s:
            if ch not in ptr.children:
                return False
            ptr = ptr.children[ch]
        return ptr.eow
            

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        max_size = len(max(wordDict, key = len))

        @cache
        def bt(l,r):
            if r == len(s) and l == r:
                return True
            while r <= l + max_size and r < len(s):
                if not trie.startsWith(s[l:r+1]):
                    return False
                if trie.contains(s[l:r+1]):
                    if (bt(r+1, r+1)):
                        return True
                r += 1
            return False
        return bt(0,0)