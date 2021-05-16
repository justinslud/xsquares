# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)

class TrieNode:
      
    # Trie node class
    def __init__(self):
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

class Trie:
      
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
      
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
          
        # private helper function
        # Converts key current character into index
        # modified to only use upper case [[[use only 'a' through 'z' and lower case]]]
          
        return ord(ch)-ord('A')

    def _indexToChar(index):
        return chr(ord('A') + index)
  
  
    def insert(self,key):
          
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
  
        # mark last node as leaf
        pCrawl.isEndOfWord = True
  
    def search(self, key):
          
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        # modified return statement to return a match for partial words as well
        # return pCrawl != None # and pCrawl.isEndOfWord
        return True
    # def search_partial(self, key):
    #     pcrawl = self.root
    #     length = 

    def count_children(self, node):
        return sum([(child is not None) for child in node.children])

    def count_remaining_nodes(self, node):
        count = 0
        pCrawl = node
        if pCrawl.isEndOfWord:
            return 0

        else:
            count += self.count_children(node)
            for child in node.children:
                if child is not None and not child.isEndOfWord:
                    count += 1
                    count += count_remaining_nodes(child)
        
        return count

    def get_node(self, key):
        # almost identical to search method, except returns a node

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]

        return pCrawl

    # returns iterator of words
    def get_remaining_nodes(self, node, substring=''):
        pCrawl = node
        if pCrawl.isEndOfWord:
            return 0

        else:
            for child in pCrawl.children:
                if child is not None:
                    yield child

        # for level in range(self.n - length):
            # substring = '' # need to collect indices and transform to letters
        for i, child in enumerate(pCrawl.children):
            if child is not None:
                substring += self._indexToChar(i)
                if child.isEndOfWord:
                    yield substring
                else:
                    self.get_remaining_nodes(child, substring)
        # pCrawl = pCrawl.children[index]


    def xsquare_with_best_addition(self, xsquare, axis, i):
        words = xsquare.rows if axis == 0 else xsquare.cols
        word = words[i]

        partial_words = words[i:]

        while True:
            test_word = next(self.get_remaining_nodes(self.get_node(word)))
            test_square = xsquare
            print(test_word)
            print(test_square)
            test_square.set(i, word, axis=axis)

            if test_square.is_valid():
                return test_square

    def most_probable_rows(self, xsquare, row_num, num=1):
        possible_xsquares = []
        for i in range(num):
            pass

        return possible_xsquares            


