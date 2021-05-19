from trie import TrieNode, Trie
import argparse
import csv

def create_trie(words):
    t = Trie()

    for word in words:
        t.insert(word)

    return t

class Xrectangle:
    def __init__(self, w, h, words=None, axis=0):
        self.w = w
        self.h = h
        self.num_descendants_axis = 0 
        
        if words:
            for i, word in enumerate(words):
                self.set(i, word, axis)
        else:
            self.rows = [''] * h
            self.cols = [''] * w

    def set(self, i, word, axis):
        if axis == 0:
            self.set_row(i, word)
        else:
            self.set_col(i, word)

    def set_row(self, row_num, word):
        self.rows[row_num] = word
        for i in range(len(word)):
            # if col is filled, do not add to it
            if len(self.cols[i]) != self.h:
                self.cols[i] += word[i]

    def set_col(self, col_num, word):
        self.cols[col_num] = word
        for i in range(len(word)):
            # if row is filled, do not add to it
            if len(self.rows[i]) != self.w:
                self.rows[i] += word[i]

    def has_no_duplicates(self):
        rows = [row for row in self.rows if len(row.strip()) == self.w]
        cols = [col for col in self.cols if len(col.strip()) == self.h] 
        return len(set(rows).union(set(cols))) == len(rows) + len(cols)

    def is_valid(self, axis):
        # checks all words along axis are in the trie
        words = self.rows if axis == 0 else self.cols
        t = t_w if axis == 0 else t_h
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

def create_rectangles(words_w, words_h, w, h, t_w, t_h, num=1, start_index=0):
    # assume w > h
    complete_rectangles = []

    for word in words_w[start_index:]:
        print(word)
        xrectangle = Xrectangle(w, h)
        xrectangle.set_row(0, word)
        xrectangles = [xrectangle]
        possible = True

        for i in range(0, h):
            # only adding rows to rectangle
            # if we are past the first row then add another row
            if i != 0:
                xrectangles = t_w.all_possible_xsquares(xrectangles, axis=0, i=i)
                # move onto next starting word if no more possible xrectangles
                if not xrectangles:
                    possible = False
                    break

            if i != h-1:
                xrectangles = t_h.all_possible_xsquares(xrectangles, axis=1, i=i)
                # move onto next starting word if no more possible xrectangles
                if not xrectangles:
                    possible = False
                    break

        if possible:
            print('at least one xrectangle found for', word)
            for xrectangle in xrectangles:
                complete_rectangles.append(xrectangle)
                print(xrectangle)

            if len(complete_rectangles) >= num:
                return complete_rectangles

    return complete_rectangles

parser = argparse.ArgumentParser()

parser.add_argument('-w', '--width', 
                    help='width of xrectangle',
                    action='store')

parser.add_argument('-l', '--height', 
                    help='height of xrectangle',
                    action='store')

parser.add_argument('-s', '--start_index', 
                    help='where in the word list to begin',
                    action='store',
                    type=int)

parser.add_argument('-a', '--num', 
                    help='number of xrectangles to find',
                    action='store',
                    type=int)



args = parser.parse_args()

if not args.width:
    args.w = '5'

if not args.height:
    args.w = '4'

if not args.num:
    args.num = 10

if not args.start_index:
    args.start_index = 0

path = './word_lists/30k_by_length/'
words_w = [word.strip() for word in open(path + args.width + '.txt', 'r').readlines()]
words_h = [word.strip() for word in open(path + args.height + '.txt', 'r').readlines()]
t_w = create_trie(words_w)
t_h = create_trie(words_h)

def save_to_csv(xrectangles, w, h):
    with open('./output/' + w + 'x' + h + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')  
        writer.writerows([xrectangle.rows for xrectangle in xrectangles])

def main():
    xrectangles = create_rectangles(words_w, words_h, w=int(args.width), h=int(args.height), t_w=t_w, t_h=t_h, num=args.num, start_index=args.start_index)

    for xrectangle in xrectangles:
        print(xrectangle, '\n')

    if len(xrectangles) >= 10:
        save_to_csv(xrectangles, args.width, args.height)

if __name__ == '__main__':
    main()