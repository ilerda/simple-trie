from trie import Trie

def main():
    trie = Trie()
    print("Inserting some words into the Trie: "
          "dog, donut, ball, do")
    trie.insert("dog")
    trie.insert("donut")
    trie.insert("ball")
    trie.insert("do")
    print("Checking prefixes")
    print("Contains 'do'?")
    print(trie.has_prefix("do"))
    print("Contains 'ba'?")
    print(trie.has_prefix("ba"))
    print("deleting some words")
    print("delete 'do'")
    trie.delete("do")
    print("delete 'ball'")
    trie.delete("ball")
    print("Check prefixes again")
    print("Contains 'do'?")
    print(trie.has_prefix("do"))
    print("Contains 'ba'?")
    print(trie.has_prefix("ba"))

if __name__ == "__main__":
    main()
