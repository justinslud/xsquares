from trie import TrieNode, Trie
import argparse
import csv

def create_trie(words):
    t = Trie()

    for word in words:
        t.insert(word)

    return t

class Xsquare:
    def __init__(self, n=5, words=None, axis=None):
        self.n = n
        self.num_descendants_axis = 0 
        
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

    # def is_complete(self):
    #     # checks all rows and cols are length n
    #     return all([len(row) == self.n for row in self.rows] + [len(col) == self.n for col in self.cols])

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


    def __str__(self):
        # used when printing grid
        string = ''
        for word in self.rows:
            # print(' '.join(word))
            string += ' '.join(word) + '\n'
        return string


def create_squares(words, n, t, num=1, start_index=1):
    complete_squares = []

    for word in words[start_index:]:
        print(word)
        xsquare = Xsquare(n)
        xsquare.set_row(0, word)
        xsquares = [xsquare]
        possible = True

        for i in range(0, n):
            # if we are past the first row then add another row
            if i != 0:
                xsquares = t.all_possible_xsquares(xsquares, axis=0, i=i)
                # move onto next starting word if no more possible xsquares
                if not xsquares:
                    possible = False
                    break
            
            # if we are before the last column then add another column
            if i != n-1:
                xsquares = t.all_possible_xsquares(xsquares, axis=1, i=i)
                if not xsquares:
                    possible = False
                    break

        if possible:
            print('at least one xsquare found for', word)
            for xsquare in xsquares:
                complete_squares.append(xsquare)
                print(xsquare)

            if len(complete_squares) >= num:
                return complete_squares

        # else:
            # print('no xsquare for', word)

    return complete_squares

# GLOBALS

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--n', 
                    help='size of xsquare',
                    action='store')

parser.add_argument('-s', '--start_index', 
                    help='where in the word list to begin',
                    action='store',
                    type=int)

parser.add_argument('-a', '--num', 
                    help='number of xsquares to find',
                    action='store',
                    type=int)

args = parser.parse_args()

if not args.n:
    args.n = '5'

if not args.num:
    args.num = 10

if not args.start_index:
    args.start_index = 0

path = './word_lists/30k_by_length/'
words = [word.strip() for word in open(path + args.n + '.txt', 'r').readlines()]
t = create_trie(words)

def save_to_csv(xsquares, n):
    with open('./output/' + n + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        # for xsquare in xsquares:
        #     writer.writerow(xsquare.rows)   
        writer.writerows([xsquare.rows for xsquare in xsquares])

def main():
    xsquares = create_squares(words, n=int(args.n), t=t, num=args.num, start_index=args.start_index)

    for xsquare in xsquares:
        print(xsquare, '\n')

    if len(xsquares) >= 10:
        save_to_csv(xsquares, args.n)

if __name__ == '__main__':
    main()