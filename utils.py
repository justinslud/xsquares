from collections import defaultdict


def xword_to_md(words):
    # Converts into markdown table format
    length = len(words[0])
    md = '|' + ' <!-- --> |' * length + '\n' + '|' + ' - |' * length + '\n'

    for word in words:
        md += '| ' + ' | '.join(word) + ' |\n'

    return md

vowels = ['A', 'E', 'I', 'O', 'U']

dot = lambda x, y: sum([x[i]*y[i] for i in range(len(x))])

def get_cnums(words, n):
    cnums = defaultdict(lambda:0)
    powers = [2**i for i in range(n-1, -1, -1)]

    for word in words:
        cword = [int(letter not in vowels) for letter in word]
        cnums[dot(powers, cword)] += 1

    return cnums

def get_clists(words):
    clists = []

    for word in words:
        clists.append([str(int(letter in vowels)) for letter in word])
    return clists

# words = [line.strip() for line in open('../word_lists/30k_by_length/5.txt').readlines()]
# print(get_cnums(words, 5))  

a = ['ABBESS', 'BURNET', 'STIGMA', 'EAGLET', 'INHUME', 'LETTER']

# print(xword_to_md(a))


import os

def split_to_files(filename, outpath):
    # outpath should have '/' at the end

    # create list to hold words
    words = []
    for length in range(30):
        words.append([])

    with open(filename, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            words[len(word)].append(word)

    os.mkdir(outpath)

    for length, words_length_n in enumerate(words):
        if words_length_n != []:
            with open(outpath + str(length) + '.txt', 'w') as o:
                for word in words_length_n:
                    o.write(word + '\n')

# split_to_files('../word_lists/30k.txt', '../word_lists/30k_by_length/')



def combine_lists(file1, file2, outfile):
    # does not check for length
    # assumes same case
    
    with open(file1, 'r') as f1:
        list1 = f1.readlines()
    
    with open(file2, 'r') as f2:
        list2 = f2.readlines()

    with open(outfile, 'w') as o:
        unique_words = set(list1).intersection(set(list2))
        o.writelines(unique_words)
