from trie import Trie

def test_descendants():
    words = ['THIS', 'THAT', 'HACK', 'TREK', 'THIN']
    t = Trie()
    for word in words:
        t.insert(word)

    # t.count_descendants_all(t.root)

    # assert t.get_node('TH').num_descendants == 3
    assert t.count_descendants(t.get_node('TH')) == 3
    # assert t.get_node('T').num_descendants == 4
    # assert t.get_node('HACK').num_descendants == 0
    # assert t.get_node('HAC').num_descendants == 1

def main():
    test_descendants()

if __name__ == '__main__':
    main()