from trie import TrieNode, Trie
# from ngrams import open_bigrams, open_trigrams
# from operator import concat
from functools import reduce

ITER_LIMIT = 1e8

def charToIndex(ch):
    return ord(ch)-ord('A')

def indexToChar(index):
    return chr(ord('A') + index)

def create_trie(words):
    t = Trie()

    for word in words:
        t.insert(word)

    return t

class Xsquare:
    # assumes we fill in xsquare alternating rows and cols
    def __init__(self, n=5, words=None, axis=None):
        self.n = n
        
        if words:
            for i, word in enumerate(words):
                self.set(i, word, axis)
        else:
            self.rows = [''] * n
            self.cols = [''] * n

    def set(self, i, word, axis):
        if axis == 0:
            self.set_row(i, word)
        else:
            self.set_col(i, word)

    def set_row(self, row_num, word):
        self.rows[row_num] = word
        for i in range(len(word)):
            # if col is filled, do not add to it
            if len(self.cols[i]) != self.n:
                self.cols[i] += word[i]

    def set_col(self, col_num, word):
        self.cols[col_num] = word
        for i in range(len(word)):
            # if row is filled, do not add to it
            if len(self.rows[i]) != self.n:
                self.rows[i] += word[i]

    def is_complete(self):
        # checks all rows and cols are length n
        return all([len(row) == self.n for row in self.rows] + [len(col) == self.n for col in self.cols])

    def has_no_duplicates(self):
        rows = [row for row in self.rows if len(row.strip()) == self.n]
        cols = [col for col in self.cols if len(col.strip()) == self.n] 
        # return len(set(self.rows).intersection(set(self.cols))) == 2 * self.n
        return len(set(rows).union(set(cols))) == len(rows) + len(cols)

    def is_valid(self, axis):
        # checks all words along axis are in the trie
        words = self.rows if axis == 0 else self.cols
        for word in words:
            if not t.search(word):
                return False

        return True

    # can always check bigrams after first row and column added
    def bigram_score(self, axis, i):
        score = 0
        words = self.rows if axis == 0 else self.cols
        for word in words:
            score += bigrams[word[i-1 : i]]

        return score / len(words)

    # must have at least 3 chars before checking trigram
    def trigram_score(self, axis, num):
        words = self.rows if axis == 0 else self.cols

    def ngram_score(self, axis, num):
        return trigram_score + bigram_score


    def __str__(self):
        # used when printing grid
        string = ''
        for word in self.rows:
            # print(' '.join(word))
            string += ' '.join(word) + '\n'
        return string


def create_squares(words, n, t, num=1, limit=ITER_LIMIT, start_index=0):
    # prints last word used as first row before returning

    iterations = 1
    complete_squares = []

    for word in words[start_index:]:
        print(word)
        xsquare = Xsquare(n)
        xsquares = [xsquare]
        possible = True
        xsquare.set_row(0, word)

        for i in range(0, n):
            iterations += 1

            # if we are past the first row then add another row
            if i != 0:
                # xsquare = t.xsquare_with_best_addition(xsquare, axis=0, i=i)
                xsquares = t.all_possible_xsquares(xsquares, axis=0, i=i)
                if not xsquares:
                    possible = False
                    break
            
            # if we are before the last column then add another column
            if i != n-1:
                # xsquare = t.xsquare_with_best_addition(xsquare, axis=1, i=i)
                xsquares = t.all_possible_xsquares(xsquares, axis=1, i=i)
                if not xsquares:
                    possible = False
                    break

        if possible:
            for xsquare in xsquares:
                if xsquare.is_complete() and xsquare.has_no_duplicates():
                    # print(xsquare)
                    complete_squares.append(xsquare)

                    if len(complete_squares) == num:
                        return complete_squares

        if iterations >= ITER_LIMIT:
            print(word)
            return complete_squares

        else:
            print('no xsquare for', word)

    return complete_squares

# GLOBALS

path = './word_lists/30k_by_length/' # hardcoded for now
words = [word.strip() for word in open(path + '4' + '.txt', 'r').readlines()]
t = create_trie(words)

def main():
    # bigrams = open_bigrams
    # trigrams = open_trigrams

    xsquares = create_squares(words, n=4, t=t, num=1)

    for xsquare in xsquares:
        print(xsquare, '\n')

if __name__ == '__main__':
    main()