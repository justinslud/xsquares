# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)

from copy import deepcopy

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

    def _indexToChar(self, index):
        # opposite of charToIndex
        # ex) indexToChar(3) -> 'D'
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
        # Counts all non-null first level children
        # Returns a number between 0 and 26
        return sum([(child is not None) for child in node.children])

    def count_remaining_nodes(self, node):
        # Counts non-null children on all levels
        count = 0
        pCrawl = node
        if pCrawl.isEndOfWord:
            return 0

        else:
            count += self.count_children(node)
            for child in node.children:
                if child is not None and not child.isEndOfWord:
                    count += 1
                    count += self.count_remaining_nodes(child)
        
        return count

    def get_node(self, key):
        # almost identical to self.search, except returns a node

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return None
            pCrawl = pCrawl.children[index]

        return pCrawl
    
    def get_remaining_nodes(self, node, length, substring=''):
        pCrawl = node

        if pCrawl.isEndOfWord:
            yield ''

        for index, child in enumerate(pCrawl.children):
            if child is not None:
                for other in self.get_remaining_nodes(child, length, substring=''):
                    yield self._indexToChar(index) + other


    def xsquare_with_best_addition(self, xsquare, axis, i):
        # Returns an Xsquare with a new row or col

        words = xsquare.rows if axis == 0 else xsquare.cols
        word = words[i]

        for test_substring in self.get_remaining_nodes(self.get_node(word),xsquare.n-i-axis):
            if not test_substring: return None
            test_word = word + test_substring
            test_square = deepcopy(xsquare)
            test_square.set(i, test_word, axis=axis)
            print(test_square)

            if test_square.is_valid(axis=abs(1-axis)):
                return test_square

    def all_possible_xsquares(self, xsquares, axis, i):
        possible_xsquares = []
        num_xsquares = len(xsquares)
        
        for xsquare in xsquares:
            words = xsquare.rows if axis == 0 else xsquare.cols
            word = words[i]

            for test_substring in self.get_remaining_nodes(self.get_node(word),xsquare.n-i-axis):
                if not test_substring: break
                test_word = word + test_substring
                test_square = deepcopy(xsquare)
                test_square.set(i, test_word, axis=axis)

                if test_square.is_valid(axis=abs(1-axis)) and test_square.has_no_duplicates():
                    possible_xsquares.append(test_square)
                    # limit possible_xsquare to 5x-ing each time
                    if len(possible_xsquares) > 10000:
                        return possible_xsquares

            xsquares.remove(xsquare)

        return possible_xsquares

    def most_probable_rows(self, xsquare, row_num, num=1):
        possible_xsquares = []
        for i in range(num):
            pass

        return possible_xsquares            


